#!/usr/bin/env python
__author__ = 'limone81'
__version__ = '1.3'
__status__ = 'dev'

### imports
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment
import os
from zipfile import ZipFile

### variables
modDesc = '../FS22_ModDependency/modDesc.xml'
modsHub = []
titleHub = []
dlc = []
titleDlc = []
modsOther = []
titleOther = []

### main
os.path.abspath

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
tree2 = ET.parse(modDesc)
root2 = tree2.getroot()


# get position of subelement
getPos = tree2.find('dependencies')

# clean old dependencies for next run
oldDepends = getPos.findall('dependency')
x = 0
for i in oldDepends:
    getPos.remove(oldDepends[x])
    x += 1

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
tree2.write(modDesc, encoding='utf-8', xml_declaration=True)

# create zipfile FS22_ModDependency.zip
with ZipFile('../FS22_ModDependency/FS22_ModDependency.zip', 'w') as zip_object:
   # files to be zipped (filepath, path_in_archive)
   zip_object.write('../FS22_ModDependency/modDesc.xml','modDesc.xml')
   zip_object.write('../FS22_ModDependency/store.dds', 'store.dds')
zip_object.close()

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


