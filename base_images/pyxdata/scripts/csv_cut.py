#!/usr/bin/python

import sys,os,re,getopt
import csv

def usage():
  print """
NAME
    csv_cut.py - Equivalent to unix cut for csv with escape characters.

SYNOPSIS
    python csv_cutpy -f 1,2,10 [-i] input.csv

DESCRIPTION
    -f List of fields to include (one-based). Ranges (e.g. "1-") not supported.
""".strip()

def cut(filename, fields, quote_char):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=quote_char)
        for row in reader:
            print ','.join(map(str.strip,[row[i] for i in range(len(row)) if not fields or str(i+1) in fields]))

optlist,args = getopt.getopt(sys.argv[1:], 'hf:', ['help'])

opts = {'quote_char': '"'}
opts.update([(key.strip('-'),value) for key,value in optlist])

if 'h' in opts or 'help' in opts or len(args) < 1:
  usage()
  sys.exit(1)

filename = args[0]
fields = opts.get('f',None)

cut(filename, fields, opts['quote_char'])
