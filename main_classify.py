#hauptdatei zum klassifizieren neuer texte, ruft funktionen zum extrahieren und bereinigen aus pdf-dateien und klassifizieren unter verwendung des vektorisierers und des modells auf

import os
from Scripts.pdf_processor import process_pdf
import joblib
from Scripts.classify import classify_text

def classify_text_from_file(model_path, vectorizer_path, file_path):
    # lesen des textes aus der datei
    with open(file_path, 'r', encoding='utf-8') as file:
        new_text = file.read()
    
    # klassifizierung
    label = classify_text(model_path, vectorizer_path, new_text)
    return label

# pfade zu modellen und der pdf-datei
model_path = 'Projekt/ML/models/ddc_model.pkl'
vectorizer_path = 'Projekt/ML/models/vectorizer.pkl'
pdf_path = 'Projekt/neuer_text.pdf' #zu klassifizierender text
output_txt_path = 'Projekt/diss_processed.txt' #wird bei extrahieren und bereinigen des textes erstellt

# verarbeiten der pdf-datei und speichern des textes
process_pdf(pdf_path, output_txt_path)

# klassifizierung des textes aus der datei unter output_txt_path
label = classify_text_from_file(model_path, vectorizer_path, output_txt_path)
print(f'Die vorhergesagte Kategorie ist: {label}')
