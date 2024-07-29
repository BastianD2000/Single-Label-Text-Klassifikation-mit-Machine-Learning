#alle pdfs der dissertationen durchlaufen, text extrahieren und bereinigen, txtfiles erstellen
"""""

import pdfminer.high_level
import os
import re

def is_table_line(line): #prüft ob tabelle
    return bool(re.search(r'\d{2,}', line))

def is_toc_line(line): #prüft ob inhaltsverzeichnis
    return bool(re.search(r'(Kapitel|Chapter|Section)\s+\d+.*\d{1,3}$', line))

def is_math_formula(line): #prüft ob mathematische formel
    return bool(re.search(r'[=+\-*/^(){}\[\]<>]', line)) or bool(re.search(r'\b(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega)\b', line, re.IGNORECASE))

def is_fragmented_line(line):
    # prüft auf zeilen mit vielen isolierten buchstaben oder kurzen fragmenten
    if len(line) < 30 and len(line.split()) < 5:
        return True
    # zeilen, die hauptsächlich zahlen oder wenige wörter enthalten
    if bool(re.match(r'^\W*\d+\W*$', line)):
        return True
    return False

def clean_extracted_text(text):
    cleaned_lines = []
    current_block = []
    
    for line in text.splitlines():
        if not is_table_line(line) and not is_toc_line(line) and not is_math_formula(line) and not is_fragmented_line(line):
            current_block.append(line)
        else:
            if current_block:
                cleaned_lines.append(" ".join(current_block))
                current_block = []
    
    if current_block:
        cleaned_lines.append(" ".join(current_block))
    
    return "\n\n".join(cleaned_lines)

# verzeichnis, in dem die dissertationen gespeichert sind durchlaufen
input_directory = 'dissertations'

for root, dirs, files in os.walk(input_directory):
    for filename in files:
        if filename.endswith(".pdf"):
            try:
                pdf_path = os.path.join(root, filename)
                print(f"Verarbeite Datei: {pdf_path}")

                filename_without_extension = os.path.splitext(filename)[0]
                txt_path = os.path.join(root, f"{filename_without_extension}.txt")
                
                text = pdfminer.high_level.extract_text(pdf_path)
                print(f"Text extrahiert aus: {pdf_path}")

                cleaned_text = clean_extracted_text(text)
                
                with open(txt_path, "w", encoding="UTF-8") as output_text_file: #bereinigten text in txtfile speichern
                    output_text_file.write(cleaned_text)
                print(f"Text gespeichert in: {txt_path}")

            except pdfminer.pdfparser.PDFSyntaxError as e:
                print(f"Fehler beim Verarbeiten der Datei {pdf_path}: {e}")
            except Exception as e:
                print(f"Ein unerwarteter Fehler trat auf beim Verarbeiten der Datei {pdf_path}: {e}")

"""""