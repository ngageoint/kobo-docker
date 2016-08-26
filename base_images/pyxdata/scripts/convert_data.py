#!/usr/bin/python
"""
Utility for converting Excel and CSV data for ODK Collect and Enketo.

Features:

- Escapes ampersand (&) characters 
- Adds lat/lon columns for MGRS coordinates
"""
import sys,os,re
import getopt
import xlrd
import mgrs
import csv
import logging

def process_excel(filename, output, default_zone, skip_mgrs=False):
  if not os.path.exists(output):
    os.mkdir(output)
  
  workbook = xlrd.open_workbook(filename)
  for sheet in [sheet for sheet in workbook.sheets() if sheet.nrows]:
    output_filename = '%s/%s.csv' % (output, sheet.name)
    getHeader = lambda: [name for name in map(str, sheet.row_values(0)) if name]
    getNumRows = lambda: sheet.nrows-1
    getRow = lambda row: sheet.row_values(row+1)
    process(output_filename, getHeader, getNumRows, getRow, default_zone, skip_mgrs)

def process_csv(filename, output, default_zone, quote_char):
  print 'CSV input not yet supported'

def process(output_filename, getHeader, getNumRows, getRow, default_zone, skip_mgrs):
  csv_file = open(output_filename,'wb')
  writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
  
  header = getHeader()
  ncols = len(header)    
  
  mgrsIndices = [i for i in range(len(header)) if header[i].lower() in ['mgrs','utm']]
  if not skip_mgrs and not mgrsIndices:
    logging.info('No MGRS column found')
    mgrsIndex = None
  elif not skip_mgrs:
    if len(mgrsIndices) > 1:
      logging.warn('Multiple MGRS columns found. Using first')
    
    mgrsIndex = mgrsIndices[0]
    header.insert(mgrsIndex+1, 'Lon')
    header.insert(mgrsIndex+1, 'Lat')
  else:
    mgrsIndex = None
  
  writer.writerow(header)
  
  for row in range(getNumRows()):
    values = [value.replace('&','&amp;') for value in map(str, getRow(row))][:ncols]
    
    if mgrsIndex:
      mgrsRaw = values[mgrsIndex].strip()
      lat = lon = ''
      patterns = [p for p in mgrs_patterns if p.match(mgrsRaw)]
      for p in patterns:
        m = p.match(mgrsRaw)
        if 'zone' in m.groupdict():
          zone = m.group('zone')
        elif default_zone:
          zone = default_zone
        else:
          continue
        
        id = m.group('id')
        easting = m.group('easting').ljust(5,'0')
        northing = m.group('northing').ljust(5,'0')
        mgrs = zone+id+easting+northing
        try:
          lat,lon = mgrs_converter.toLatLon(mgrs)
        except Exception, e:
          logging.warn('Error converting MGRS %s (%s): %s' % (mgrsRaw, mgrs, e))
      
      if mgrsRaw and not patterns:
        logging.debug('No matching MGRS patterns for \'%s\'' % mgrsRaw)
      elif not mgrsRaw and [p for p in patterns if 'zone' in p.match(mgrsRaw).groupdict() or default_zone != None]:
        logging.debug('Zone not found and no default for \'%s\'' % mgrsRaw)
      
      values.insert(mgrsIndex+1, str(lon))
      values.insert(mgrsIndex+1, str(lat))
    
    writer.writerow(values)
  
  csv_file.close()

def usage():
  print """
NAME
    convert_data.py - Utility for converting Excel and CSV data for ODK Collect and Enketo.

SYNOPSIS
    python convert_data.py [--zone mgrs_zone] input.xlsx output_dir
""".strip()

mgrs_converter = mgrs.MGRS()
mgrs_patterns = [re.compile('(?P<id>[A-Z]{2})\s*(?P<easting>\d{3})\s*(?P<northing>\d{3})\s*')]

optlist,args = getopt.getopt(sys.argv[1:], 'hv', ['zone=','help=','verbose=','quote_char=','skip_mgrs'])

opts = {'quote_char': '"',
	'zone': None}
opts.update([(key.strip('-'),value) for key,value in optlist])

level = (logging.INFO, logging.DEBUG)[int('v' in opts or 'verbose' in opts)]
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=level)

if len(args) < 2:
  print 'Missing required filename argument(s)'

if 'h' in opts or 'help' in opts or len(args) < 2:
  usage()
  sys.exit(1)

filename,output = args[:2]
skip_mgrs = 'skip_mgrs' in opts

if not os.path.exists(filename) or filename.split('.')[-1] not in ['csv','xlsx','xls']:
  print 'File not found or unrecognized extension: %s' % filename
  sys.exit(1)

if filename.split('.')[-1] in ['xlsx','xls']:
  process_excel(filename, output, opts['zone'], skip_mgrs=skip_mgrs)
else:
  process_csv(filename, output, opts['zone'], opts['quote_char'], skip_mgrs=skip_mgrs)

