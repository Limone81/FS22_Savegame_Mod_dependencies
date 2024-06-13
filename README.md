# FS22_Savegame_Mod_dependencies
## Autoload von Modhub-Mods für Farming Simulator 22 Savegames

Dieses Tool ermöglicht es, aus einem bestehenden Savegame die Mods (sofern im Modhub verfügbar) zu ermitteln, die bei einer Weitergabe des Spielstandes notwendig sind. Diese können dann in Form eines eigenen Mods als Abhängigkeit in den Modordner gepackt werden. 

Die ermittelten Mods werden in einer eigenen XML-Datei gespeichert. Diese werden dort sortiert, basierend auf den Anfangsbuchstaben des Modnamens. Alle Mods die mit "FS22" beginnen werden dabei zusammengefasst, ebenso wie die benutzten DLC die separat gelistet werden. 
Mods die nicht mit "FS22" beginnen werden als "none Modhub Mods" klassifiziert und gesondert ausgegeben. Wenn Mods mit "FS22" im Modnamen beginnen aber dennoch nicht aus dem Modhub stammen, funktioniert dass an der Stelle nicht und die Information dazu muss separat erfolgen, ebenso die Herkunft derer.

Damit das Ganze dann als Mod geladen werden kann, müssen die "Modhub Mods" in die modDesc an der kommentierten Stelle eingefügt werden.

### Ablauf
1. Kopiere die Datei aus dem /exe Odner an den Pfad, an der sich die **careerSavegame.xml** befindet (in der Regel ist das ein Savegame Ordner z.B. FarmingSimulator2022\savegame1) oder packe beide zusammen in einen separaten Ordner
2. führe die *.exe per Doppelklick aus, es wird eine **dependencies.xml** erzeugt
3. öffne die dependencies.xml und die modDesc.xml aus FS22_ModDependency
4. kopiere die als Modhub Mods erkannten Mods aus der dependencies.xml in die modDesc.xml an die kommentiert Stelle
5. speichere die modDesc.xml mit den Änderungen
6. zippe die modDesc.xml sowie die Bilddatei in dem Ordner FS22_ModDependency (Dateiformat zip, kein rar und kein 7z)
7. kopiere die FS22_ModDependency.zip in deinen Modordner
8. konfiguriere das erhaltenen Savegame in deinem **FarmingSimulator2022** Ornder
9. Starte den Farmin Simulator 22 und lade das Savegame, die benötigten Mods sollten als Popup angezeigt werden mit der Möglichkeit diese zu laden


## English description

This tool makes it possible to determine the mods (if available in the Modhub) from an existing savegame that are required when the savegame is passed on. These can then be packed into the mod folder as a dependency in the form of a custom mod. 

The determined mods are saved in a separate XML file. They are sorted there based on the first letter of the mod name. All mods beginning with "FS22" are grouped together, as are the DLCs used, which are listed separately. 
Mods that do not start with "FS22" are classified as "none Modhub Mods" and listed separately. If mods begin with "FS22" in the mod name but do not originate from the Modhub, this will not work at this point and the information on this must be provided separately, as must the origin of the mods.

So that the whole thing can then be loaded as a mod, the "Modhub mods" must be inserted into the modDesc at the commented location.

### Procedure
1. copy the file from the /exe folder to the path where the **careerSavegame.xml** is located (usually this is a savegame folder e.g. FarmingSimulator2022\savegame1) or put both together in a separate folder
2. execute the *.exe by double-clicking, a **dependencies.xml** will be created
3. open the dependencies.xml and the modDesc.xml from FS22_ModDependency
4. copy the mods recognized as Modhub mods from the dependencies.xml into the modDesc.xml at the commented location
5. save the modDesc.xml with the changes
6. zip the modDesc.xml and the image file into the folder FS22_ModDependency (file format zip, no rar and no 7z)
7. copy the FS22_ModDependency.zip into your mod folder
8. configure the received savegame in your **FarmingSimulator2022** folder
9. start Farmin Simulator 22 and load the savegame, the required mods should be displayed as a popup with the option to load them
