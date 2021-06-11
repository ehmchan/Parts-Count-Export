import xml.etree.ElementTree as ET
import csv

tree = ET.parse('parts_count.xml')
root = tree.getroot()

events = root.find('events')
event = events.findall('event')
for child in event:
    id = child.find('id')
    parts_count = child.find('parts-count')
    print(id.text)
    for part in parts_count:
        description = part.find('part-description')
        print(description.text)
        count = part.find('count')
        print(count.text)
    print('\n')

