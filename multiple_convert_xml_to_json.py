import xmltodict, json
import os
import re

for exists in os.listdir('/directory_to_xml_file/'):
    exists = re.findall("(.*xml$)", exists)
    for xml in exists:
        with open("/directory_to_xml_file/"+xml, 'rw') as fin:
            xml = xml.split('.')[0]
            obj = open('/directory_to_xml_file/{}.json'.format(xml), 'wb')
            doc = xmltodict.parse(fin.read())
            data = json.dumps(doc, indent=True)
            obj.write(data)
