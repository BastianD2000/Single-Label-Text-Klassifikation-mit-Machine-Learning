import pdfminer.high_level
import re
import os

def is_table_line(line): #prüfen ob zeile eine tabellenzeile ist
    return bool(re.search(r'\d{2,}', line)) #indestens zwei aufeinanderfolgende ziffern

def is_toc_line(line):
    return bool(re.search(r'(Kapitel|Chapter|Section)\s+\d+.*\d{1,3}$', line)) #prüft ob inhaltsverzeichnis

def is_math_formula(line): #prüft ob mathematische formel mit formelzeichen, griechischen buchstaben
    return bool(re.search(r'[=+\-*/^(){}\[\]<>]', line)) or bool(re.search(r'\b(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega)\b', line, re.IGNORECASE))

def is_fragmented_line(line): # prüft auf Zeilen mit vielen isolierten buchstaben oder kurzen fragmenten
    if len(line) < 30 and len(line.split()) < 5:
        return True
    if bool(re.match(r'^\W*\d+\W*$', line)): # prüft auf zeilen, die hauptsächlich zahlen oder wenige wörter enthalten
        return True
    return False

def clean_extracted_text(text): #extrahierten text bereinigen
    cleaned_lines = [] #gereinite textblöcke speichern
    current_block = [] #aktueller textblock kurz speichern
    
    for line in text.splitlines():
        if not is_table_line(line) and not is_toc_line(line) and not is_math_formula(line) and not is_fragmented_line(line):
            current_block.append(line) #fügt aktuellen zeile zu block in temporärer liste, wenn nichts zutrifft
        else:
            if current_block:
                cleaned_lines.append(" ".join(current_block)) #fügt aktuellen block zur bereinigeten liste
                current_block = [] #temporäre liste leeren
    
    if current_block:
        cleaned_lines.append(" ".join(current_block))
    
    return "\n\n".join(cleaned_lines) #gibt bereinigten text als string zurück

def process_pdf(pdf_path, output_txt_path): #funktion zur verarbeitung pdf
    try:
        print(f"Verarbeite Datei: {pdf_path}")
        
        text = pdfminer.high_level.extract_text(pdf_path) #extrahiert text
        print(f"Text extrahiert aus: {pdf_path}")

        cleaned_text = clean_extracted_text(text) #bereinigt text
        
        with open(output_txt_path, "w", encoding="UTF-8") as output_text_file: #öffnet ausgabedatei
            output_text_file.write(cleaned_text) #schreibt bereinigten text in ausgabedatei
        print(f"Text gespeichert in: {output_txt_path}")

    except pdfminer.pdfparser.PDFSyntaxError as e: #pdf syntaxfehler
        print(f"Fehler beim Verarbeiten der Datei {pdf_path}: {e}")
    except Exception as e: #allgemeiner fehler
        print(f"Ein unerwarteter Fehler trat auf beim Verarbeiten der Datei {pdf_path}: {e}")
