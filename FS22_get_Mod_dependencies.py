#!/usr/bin/env python
__author__ = 'limone81'
__version__ = '0.0.1'
__status__ = 'dev'

### imports
import xml.etree.ElementTree as ET

### variables
mods = []
title = []

### main
tree = ET.parse('careerSavegame.xml')
root = tree.getroot()

for element in root.iter(('mod')):
    mods.append(element.attrib['modName'])
    title.append(element.attrib['title'])

print(mods)
print(title)