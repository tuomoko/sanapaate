#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# By Tuomo Kohtamäki 13.1.2018

import xml.etree.ElementTree
import re
import argparse

# Lataa sanalista osoitteesta
# http://kaino.kotus.fi/sanat/nykysuomi/kotus-sanalista-v1.tar.gz
wordlist = 'kotus-sanalista_v1.xml'

parser = argparse.ArgumentParser(description='Etsi sanapäätteitä kotuksen listasta.')
parser.add_argument('paate', type=str, help='etsittävä pääte')
args = parser.parse_args()

if args.paate:
    ending = args.paate
    e = xml.etree.ElementTree.parse(wordlist).getroot()
    pattern = re.escape(ending)

    for record in e.findall('st'):
        word = record.findall('s')[0].text
        linematch = re.match(r'.*'+pattern+'$',word)
        if linematch:
            print(word.encode('utf-8'))

