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

# parse modDesc.xml
tree2 = ET.parse('modDesc.xml')
root2 = tree2.getroot()

# get position of subelement
getPos = tree2.find('dependencies')

# function to add subelements
def addNames(toadd, value):
    for i in toadd:
        sub = ET.Element(value)
        sub.text = i
        getPos.append(sub)


# add Modhub Mods
addNames(modsHub, 'dependency')

# get newlines after each entry for pretty look
ET.indent(tree2, space="\t", level=0)

# save tree to modDesc.xml
tree2.write('modDesc.xml', encoding='utf-8', xml_declaration=True)

def addDlcOther(toadd, title, value):
    x=0
    for i in toadd:
        add = ET.Element(value)
        add.text = i
        add.set ('title', title[x])
        root3.append(add)
        x += 1

# create new root
root3 = ET.fromstring("<item></item>")
tree3 = ET.ElementTree(root3)

# adding comment for DLC to xml
com2 = Comment('DLC')
root3.append(com2)

# add Dlc
addDlcOther(dlc, titleDlc, 'pdlc')

# adding comment for none Modhub Mods to xml
com3 = Comment('none Modhub Mods')
root3.append(com3)

# add none-Modhub Mods
addDlcOther(modsOther, titleOther, 'otherMods')

# get newlines after each entry for pretty look
ET.indent(tree3, space="\t", level=0)

# save tree to dlc_noneModhubMods.xml
tree3.write('dlc_noneModhubMods.xml', encoding='utf-8', xml_declaration=True)