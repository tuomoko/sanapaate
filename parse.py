import xml.etree.ElementTree
import re

ending = 'in'

# Lataa sanalista osoitteesta
# http://kaino.kotus.fi/sanat/nykysuomi/kotus-sanalista-v1.tar.gz
lista = 'kotus-sanalista_v1.xml'

e = xml.etree.ElementTree.parse(lista).getroot()
pattern = re.escape(ending)

for record in e.findall('st'):
    word = record.findall('s')[0].text
    linematch = re.match(r'.*'+pattern+'$',word)
    if linematch:
        print(word)
