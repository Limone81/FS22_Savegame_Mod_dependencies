# FS22_Savegame_Mod_dependencies
## Autoload von Modhub-Mods für Farming Simulator 22 Savegames

Dieses Tool ermöglicht es, aus einem bestehenden Savegame die Mods (sofern im Modhub verfügbar) zu ermitteln, die bei einer Weitergabe des Spielstandes notwendig sind. Diese können dann in Form eines eigenen Mods als Abhängigkeit in den Modordner gepackt werden. 

Die ermittelten Mods werden in einer modDesc-Datei als dependency gespeichert. Alle Mods, die mit "FS22" beginnen, werden dabei zur modDesc hinzugefügt. DLC und Mods die nicht mit "FS22" beginnen werden als "none Modhub Mods" klassifiziert und gesondert in einer xml-Datei ausgegeben. 

:warning: Wenn Mods mit "FS22" im Modnamen beginnen, aber dennoch nicht aus dem Modhub stammen, funktioniert dass an der Stelle nicht und die Information dazu muss separat erfolgen, ebenso die Herkunft derer. Die dependency Mod (FS22_ModDependency) muss dann nach dem erstmaligen laden aller "Modhub Mods" aus dem Modordner entfernt werden, da übrig geliebene Abhängigkeiten (die Mods welche nicht aus dem Modhub stammen) nicht geladen werden können und der Ladevorgang sonst mit einer Fehlermeldung abbricht!

### Ablauf
Lade die Dateien (Release) herunter und entpacke sie
1. Kopiere die **careerSavegame.xml** die ausgelesen werden soll in den Ordner **executable**
2. führe die *.exe per Doppelklick aus, die Savegame Datei wird eingelesen, die Modhub-Mods in die **modDesc.xml eingetragen** (im Ordner **FS22_ModDependency**) und es wird eine separate **dlc_noneModhubMods.xml** erzeugt, aus der die DLC- sowie "none Modhub Mods"-Namen entnommen werden können
3. im Ordner FS22_ModDependency wird automatisch eine **FS22_ModDependency.zip** erstellt
4. kopiere die FS22_ModDependency.zip in deinen Modordner
5. konfiguriere das erhaltene Savegame in deinem **FarmingSimulator2022** Ornder
6. Starte den Farming Simulator 22 und lade das Savegame, die benötigten Mods sollten als Popup angezeigt werden, mit der Möglichkeit diese zu laden

:rotating_light: Für die Experten mit 1000 Mods im Ordner hier die Warnung! Der Dependency Mod wird eine Downloadschlange initialisieren, die auch nach einem Neustart des Spieles weiter geladen wird. Wenn man diesen Prozess beenden will, muss man im  Ordner **My Games\FarmingSimulator2022\pending_downloads** die Datei pendingDownloadQueue.dat löschen.

## English description

This tool makes it possible to determine the mods (if available in the Modhub) from an existing savegame that are required when the savegame is passed on. These can then be packed into the mod folder in the form of a custom mod as a dependency. 

The mods determined are saved in a modDesc file as a dependency. All mods that begin with "FS22" are added to the modDesc. DLC and mods that do not start with "FS22" are classified as "none Modhub Mods" and output separately in an xml file. 

:warning: If mods begin with "FS22" in the mod name, but do not originate from the Modhub, this does not work at this point and the information on this must be provided separately, as must the origin of the mods. The dependency mod (FS22_ModDependency) must then be removed from the mod folder after loading all "Modhub mods" for the first time, as any remaining dependencies (the mods that do not originate from the Modhub) cannot be loaded and the loading process will otherwise abort with an error message!

### Procedure
Download the files (release) and unpack it
1. copy the **careerSavegame.xml** to be read into the **executable** folder
2. double-click the *.exe, the savegame file is read in, the modhub mods are entered in the **modDesc.xml** (in the **FS22_ModDependency** folder) and a separate **dlc_noneModhubMods.xml** is created, from which the DLC and "none Modhub Mods" names can be taken.
3. a **FS22_ModDependency.zip** is automatically created in the FS22_ModDependency folder
4. copy the FS22_ModDependency.zip into your mod folder
5. configure the received savegame in your **FarmingSimulator2022** folder
6. start Farming Simulator 22 and load the savegame, the required mods should be displayed as a popup with the option to load them

:rotating_light: For the experts with 1000 mods in their folder, here is a warning! The dependency mod will initialize a download queue that will continue to load even after restarting the game. If you want to end this process, you must delete the pendingDownloadQueue.dat file in the **My Games\FarmingSimulator2022\pending_downloads** folder.
