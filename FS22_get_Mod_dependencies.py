#!/usr/bin/env python
__author__ = 'limone81'
__version__ = '0.0.1'
__status__ = 'dev'

### imports
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment

### variables
modsHub = []
titleHub = []
dlc = []
titleDlc = []
modsOther = []
titleOther = []

### main
# parse careerSavegame.xml
tree = ET.parse('careerSavegame.xml')
root = tree.getroot()

# iter through Mods listed in careerSavegame.xml
for element in root.iter(('mod')):
    x = element.attrib['modName']
    y = element.attrib['title']
    if (x.startswith('FS22')):
        modsHub.append(x)
        titleHub.append(y)
    elif (x.startswith('pdlc')):
        dlc.append(x)
        titleDlc.append(y)
    else:
        modsOther.append(x)
        titleOther.append(y)

def addNames(toadd, value):
    for i in toadd:
        add = ET.Element(value)
        add.text = i
        root.append(add)

# create new root
root = ET.fromstring("<dependencies></dependencies>")
tree = ET.ElementTree(root)

# adding comment for Modhub Mods to xml
com1 = Comment('Modhub Mods')
root.append(com1)

# add Modhub Mods
addNames(modsHub, 'dependency')

# adding comment for DLC to xml
com2 = Comment('DLC')
root.append(com2)

# add Dlc
addNames(dlc, 'pdlc')

# adding comment for none Modhub Mods to xml
com3 = Comment('none Modhub Mods')
root.append(com3)

# add none-Modhub Mods
addNames(modsOther, 'otherMods')

# get newlines after each entry for pretty look
ET.indent(tree, space="\t", level=0)

# save tree to dependencies.xml
tree.write('dependencies.xml', encoding='utf-8', xml_declaration=True)
