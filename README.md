# FS22_Savegame_Mod_depencies
## Autoload von Modhub-Mods für Farming Simulator 22 Savegames

Dieses Tool ermöglicht es, aus einem bestehenden Savegame die Mods (sofern im Modhub verfügbar) zu ermitteln, die bei einer Weitergabe des Spielstandes notwendig sind. Diese können dann in Form eines eigenen Mods als Abhängigkeit in den Modordner gepackt werden. 

Die ermittelten Mods werden in einer eigenen XML-Datei gespeichert. Diese werden dort sortiert, basierend auf den Anfangsbuchstaben des Modnamens. Alle Mods die mit "FS22" beginnen werden dabei zusammengefasst, ebenso wie die benutzten DLC die separat gelistet werden. 
Mods die nicht mit "FS22" beginnen werden als "none Modhub Mods" klassifiziert und gesondert ausgegeben. Wenn Mods mit "FS22" im Modnamen beginnen aber dennoch nicht aus dem Modhub stammen, funktioniert dass an der Stelle nicht und die Information dazu muss separat erfolgen, ebenso die Herkunft derer.

Damit das Ganze dann als Mod geladen werden kann, müssen die "Modhub Mods" in die modDesc an der kommentierten Stelle eingefügt werden.


## English description

This tool makes it possible to determine the mods (if available in the Modhub) from an existing savegame that are required when the savegame is passed on. These can then be packed into the mod folder as a dependency in the form of a custom mod. 

The determined mods are saved in a separate XML file. They are sorted there based on the first letter of the mod name. All mods beginning with "FS22" are grouped together, as are the DLCs used, which are listed separately. 
Mods that do not start with "FS22" are classified as "none Modhub Mods" and listed separately. If mods begin with "FS22" in the mod name but do not originate from the Modhub, this will not work at this point and the information on this must be provided separately, as must the origin of the mods.

So that the whole thing can then be loaded as a mod, the "Modhub mods" must be inserted into the modDesc at the commented location.

Translated with DeepL.com (free version)
