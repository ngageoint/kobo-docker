#!/usr/bin/python

import sys,os,re,getopt
import csv

def usage():
  print """
NAME
    enketo_xml_cleanup.py - Simple XML cleanup for Enketo compatibility

SYNOPSIS
    python enketo_xml_cleanup input.xml

NOTES

Optionally first generate XML using xls2xform.py from latest pyxform. Ensure
only a single instance is created for each external data soure and also that
related itemsets have the below child elements.

<itemset nodeset="instance('cities')/...">
  <value ref="name"/>
  <label ref="label"/>
</itemset>
""".strip()

def process(filename):
    with open(filename) as fp:
        xml = fp.read()
        xml = xml.replace('name_key','name')
        xml = xml.replace("join(' '","join(', '")
        xml = xml.replace('&lt;p&gt;','').replace('&lt;/p&gt;','')
        xml = xml.replace(' appearance="compact"','')
        print xml

optlist,args = getopt.getopt(sys.argv[1:], 'h:', ['help'])

opts = {}
opts.update([(key.strip('-'),value) for key,value in optlist])

if 'h' in opts or 'help' in opts or len(args) < 1:
  usage()
  sys.exit(1)

filename = args[0]

process(filename)
