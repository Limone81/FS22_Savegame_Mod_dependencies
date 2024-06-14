# FS22_Savegame_Mod_dependencies
## Autoload von Modhub-Mods für Farming Simulator 22 Savegames

Dieses Tool ermöglicht es, aus einem bestehenden Savegame die Mods (sofern im Modhub verfügbar) zu ermitteln, die bei einer Weitergabe des Spielstandes notwendig sind. Diese können dann in Form eines eigenen Mods als Abhängigkeit in den Modordner gepackt werden. 

Die ermittelten Mods werden in einer modDesc-Datei als dependency gespeichert. Alle Mods, die mit "FS22" beginnen, werden dabei zur modDesc hinzugefügt. DLC und Mods die nicht mit "FS22" beginnen werden als "none Modhub Mods" klassifiziert und gesondert in einer xml-Datei ausgegeben. Wenn Mods mit "FS22" im Modnamen beginnen, aber dennoch nicht aus dem Modhub stammen, funktioniert dass an der Stelle nicht und die Information dazu muss separat erfolgen, ebenso die Herkunft derer.

### Ablauf
1. Kopiere die Datei aus dem /exe Odner, zusammen mit der **careerSavegame.xml** die ausgelesen werden soll und der **modDesc.xml**
2. führe die *.exe per Doppelklick aus, die Savegame Datei wird eingelesen, die Modhub-Mods in die **modDesc.xml eingetragen** und es wird eine separate **dlc_noneModhubMods.xml** erzeugt, aus der die DLC- sowie "none Modhub Mods"-Namen entnommen werden können
3. Kopiere die editierte modDesc.xml in den Ordner **FS22_ModDependency**
4. zippe die modDesc.xml sowie die Bilddatei in dem Ordner FS22_ModDependency (Dateiformat zip, kein rar und kein 7z) -> Name sollte dann **FS22_ModDependency.zip** sein
5. kopiere die FS22_ModDependency.zip in deinen Modordner
6. konfiguriere das erhaltenen Savegame in deinem **FarmingSimulator2022** Ornder
7. Starte den Farmin Simulator 22 und lade das Savegame, die benötigten Mods sollten als Popup angezeigt werden mit der Möglichkeit diese zu laden


## English description

This tool makes it possible to determine the mods (if available in the Modhub) from an existing savegame that are required when the savegame is passed on. These can then be packed into the mod folder in the form of a custom mod as a dependency. 

The mods determined are saved in a modDesc file as a dependency. All mods that begin with "FS22" are added to the modDesc. DLC and mods that do not start with "FS22" are classified as "none Modhub Mods" and output separately in an xml file. If mods begin with "FS22" in the mod name but do not originate from the modhub, this does not work at this point and the information on this must be provided separately, as must the origin of the mods.

### Procedure
1. copy the file from the /exe folder, together with the **careerSavegame.xml** to be read out and the **modDesc.xml**
2. double-click the *.exe, the savegame file is read in, the modhub mods are entered in the **modDesc.xml** and a separate **dlc_noneModhubMods.xml** is created, from which the DLC and "none Modhub Mods" names can be taken.
3. copy the edited modDesc.xml into the **FS22_ModDependency** folder
4. zip the modDesc.xml and the image file into the folder FS22_ModDependency (file format zip, no rar and no 7z) -> name should then be **FS22_ModDependency.zip**.
5. copy the FS22_ModDependency.zip into your mod folder
6. configure the received savegame in your **FarmingSimulator2022** folder
7. start Farmin Simulator 22 and load the savegame, the required mods should be displayed as a popup with the option to load them
