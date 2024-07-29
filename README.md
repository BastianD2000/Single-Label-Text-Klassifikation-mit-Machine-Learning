1. Zielsetzung
   
Ziel des Projektes war es ein Programm zu schreiben, welches unter Verwendung von Werkzeugen 
des Machine Learning auf Texte mit ihrer jeweiligen Dewey Decimal Classification (DDC) trainiert 
werden kann, um so schließlich neuen Texten eine DDC zuzuweisen.

2. Vorbereitung (Ordner „Vorarbeit“)
   
Um eine Datenmenge für die Trainings- und Testdaten zu erhalten, wurde das Repositorium der 
Technischen Universität Darmstadt (tuprints) verwendet. Auf tuprints wurde die Ergebnismenge 
nach Dissertationen gefiltert und es wurde ein Export der Metadaten aller Treffer durchgeführt. In 
dem daraus erhaltenen XML befinden sich unter anderem ein Downloadlink und die zugehörige DDC 
für jede Dissertation.
Nun wurde das Skript „extraction.py“ erstellt um das XML automatisch zu durchlaufen und dabei die 
Volltexte und ihre jeweiligen DDCs abzuspeichern. Gespeichert werden die Texte in dem Ordner 
„dissertations“, in welchem jede Dissertation einen Unterordner erhält. Hier liegen das PDF und eine 
Textdatei mit der DDC (ddc_groups.txt).
Um die Texte in weiterverwenden zu können, wurde das Skript „pdftextmine.py“ erstellt, welches 
den relevanten Text extrahiert und in einer Textdatei (text.txt) abspeichert.
Da die Textdateien mit den extrahierten Texten nun noch die ursprünglichen Dateinamen der PDFs 
hatten, wurden sie über das Skript „rename.py“ alle zu „text.txt“ umbenannt.
Da das XML bei manchen Dissertationen keine Angaben zu DDCs machte oder die Downloadlinks 
teilweise nicht funktionierten, wurden alle Dissertationen mit unvollständigen Daten über das Skript 
„complete.py“ ermittelt und gelöscht.
Da die Methode „stratify“ verlangt, dass von jeder DDC mindestens zwei im Datenset vorhanden 
sind, wurden über das Skript „count_labels.py“ alle einmaligen DDCs und ihre Dissertationen 
ermittelt. Diese wurden dann manuell aus der Datenmenge entfernt.
Es stand die Überlegung im Raum, einen Tokenizer auf die Trainings- und Testdaten anzuwenden, 
diese Idee wurde aber verworfen. Die Tokenisierung der Texte hätte keinen Mehrwert geliefert. 
Der Tokenizer befindet sich noch im Ordner „Vorarbeit“ und kann bei Interesse verwendet werden.

3. Modularer Aufbau (Ordner „Scripts“)
   
load_data.py
Dieses Skript definiert die Funktion zum Laden der Daten. Es durchläuft die Ordnerstruktur in 
„dissertations“ und lädt zu jeder Dissertation den Text und die DDC, welche jeweils einer Liste 
hinzugefügt werden. Falls mehrere DDCs für eine Dissertation vergeben wurden, wird nur die 
erstgenannte geladen.

preprocess.py
Dieses Skript erstellt einen Vektorisierer und wendet diesen auf die geladenen Texte an, um aus 
ihnen Vektoren zu erstellen.

training.py
Dieses Skript legt die Funktion für das Training des Modells fest. Hier wird dabei auch bestimmt, ob 
dafür Naive Bayes oder Support Vector Machine verwendet werden soll. Um die verwendete 
Methode zu ändern, muss die jeweils nicht gewünschte Methode in den Imports und in Zeile 13/14 
auskommentiert werden.
Außerdem erstellt dieses Skript eine Datei mit der Evaluation des Modells und berechnet dazu die 
Werte von Precision, Recall und dem F1-Score. Das Modell und der Vektorisierer werden für die 
spätere Klassifikation neuer Texte gespeichert.

evaluate.py
Dieses Skript sagt Klassifikationen für die Testdaten voraus, evaluiert sie und gibt das Ergebnis in der 
Konsole wieder.

pdf_processor.py
Dieses Skript dient dazu die PDF-Dateien der später neu zu klassifizierenden Texten zu verarbeiten. 
Dazu extrahiert und bereinigt es den Text, um ihn schließlich in einer Textdatei zu speichern. 

classify.py
Dieses Skript definiert die Funktion, welche der Klassifikation neuer Texte dient. Sie lädt das 
vortrainierte Modell und den Vektorisierer, um diese auf den neuen Text anzuwenden und eine DDC 
für diesen vorherzusagen.

4. Abruf der Funktionen

main_train.py
In diesem Skript werden die Funktionen aus „load_data.py“, „preprocess.py“ und „training.py“ 
abgerufen um alle Dissertationen aus „dissertations“ zu laden, zu vektorisieren und um basierend 
darauf das Modell zu trainieren. Zudem wird die Evaluation erstellt und im Ordner „Evaluation“ 
gespeichert.

main_classify.py
In diesem Skript werden die Funktionen aus „pdf_processor.py“ und „classify.py“ aufgerufen um, um 
ein neues PDF zu verarbeiten und basierend auf dem vortrainierten Modell zu klassifizieren. In der 
Konsole wird dann schließlich die vorhergesagte DDC angegeben. Der Pfad zu dem zu 
klassifizierenden Text wird nach „pdf_path=“ in Zeile 20 angegeben.

5. Verwendung der Skripte
   
Nachdem die Schritte zur Vorbereitung der Trainingsdaten befolgt wurden (siehe Kapitel 2), muss 
zuerst „main_train.py“ ausgeführt werden um das Modell zu trainieren. 
Anschließend muss ein neuer zu klassifizierender Text im PDF-Format im Hauptordner „Projekt“ 
abgelegt werden und sein Pfad muss in „main_classify.py“ in Zeile 20 angegeben werden (zu Testund Demonstrationszwecken liegt „neuer_text.pdf“ im Ordner „Projekt“ bereit). 
Nun kann „main_classify.py“ ausgeführt werden und man erhält in der Konsole ein Ergebnis.

6. Verwendete Hilfsmittel
Der Code wurde mit Unterstützung von ChatGPT (https://chatgpt.com/) erstellt.
Verwendet wird die Python-Bibliothek „sklearn“.
