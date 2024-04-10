# Sakai-Aufgabe-Leistungskurve

**Leistungskurve von Till Schröter; Finn Petroll**

## Benutzeranleitung
1. Laden sie das Repository mit Hilfe volgendem Link als Zip Datei herunter: https://github.com/TillSchroeter/Sakai-Aufgabe-Leistungskurve.git .
2. Verschieben sie den Zip Ordner in einen Ordner ihrer Wahl im Windowsexpolorer und entpacken sie diesen dort.
3. Gehen sie in VS-Code und öffnen sie den Entpackten Ordner unter File --> Open Folder.
4. Um ihre Pakete zu verwalten und keine Überschneidungen mit anderen Projekten zu generieren, erstellen sie eine Virtuelle Umgebung (virtual environment).
   
   4.1. Öffnen Sie das Terminal in VS Code.
   
   4.2. Geben Sie **"python -m venv .venv"** ein.
   
   4.3. Aktivieren Sie die Virtuelle Umgebung mit **"source .venv/bin/activate"** (Linux/Mac) oder **".\.venv\Scripts\Activate"** (Windows).
   
   4.4. Sie haben nun eine Virtuelle Umgebung erstellt.
   
6. Sie sollten nun einmalig die _load_data.py_ und die _sort.py_ oben rechts (Play button) ausführen, um die benötigten Funktionen einmalig zu 'implementieren'
7. Um die -powerOriginal- daten zu Plotten führen sie die _main.py_ aus. Diese Daten wurden sortiert und gegen die Zeit aufgetragen (Im Diagramm).
8. Dieser Plot wird als _Leistungskurve.png_ gespeichert. 
9. Um Veränderungen vorzunehmen und beispielsweise mit weitere Daten aus der _activity.csv_ Datei zu arbeiten, schreiben sie ihren Code in der _main.py_.



