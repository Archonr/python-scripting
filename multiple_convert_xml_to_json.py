import xmltodict, json
import os
import re

dir = "/directory_where_xml_files/"

for exists in os.listdir(dir):
    exists = re.findall("(.*xml$)", exists)
    for xml in exists:
        with open(dir+xml, 'rw') as fin:
            xml = xml.split('.')[0]
            obj = open(dir+'{}.json'.format(xml), 'wb')
            doc = xmltodict.parse(fin.read())
            data = json.dumps(doc, indent=True)
            #print data
            obj.write(data)
