#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# By Tuomo Kohtamäki 13.1.2018

import xml.etree.ElementTree
import re
import argparse

# Lataa sanalista osoitteesta
# http://kaino.kotus.fi/sanat/nykysuomi/kotus-sanalista-v1.tar.gz

parser = argparse.ArgumentParser(description='Find words ending with specific letters.')
parser.add_argument('ending', type=str, help='String to find at the end of the word')
parser.add_argument("--wordlist", default='kotus-sanalista_v1.xml', type=str, help="Add custom word list (default kotus-sanalista_v1.xml)")
args = parser.parse_args()

wordlist = args.wordlist

if args.ending:
    ending = args.ending
    e = xml.etree.ElementTree.parse(wordlist).getroot()
    pattern = re.escape(ending)

    for record in e.findall('st'):
        word = record.findall('s')[0].text
        linematch = re.match(r'.*'+pattern+'$',word)
        if linematch:
            print(word.encode('utf-8'))

