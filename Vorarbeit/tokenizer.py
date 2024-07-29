#tokenizer fand in finaler durchführung keine verwendung, kann aber gerne benutzt werden, textdateien in trainingsdaten heißen dann aber text_tokenized.txt

import os
from nltk.tokenize import word_tokenize

# pfad zum hauptordner
dataset_path = 'dissertations'


# funktion zum tokenisieren und speichern der token in einer neuen datei
def tokenize_and_save(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = word_tokenize(text, language='german')  # tokenisierung mit NLTK
        tokenized_text = ' '.join(tokens)

        # neuen dateinamen erstellen
        new_file_name = file_path.replace('.txt', '_tokenized.txt')

        # tokenisierten text in neue datei schreiben
        with open(new_file_name, 'w', encoding='utf-8') as new_file:
            new_file.write(tokenized_text)


# durch alle ordner und dateien iterieren
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file == 'text.txt':
            file_path = os.path.join(root, file)
            tokenize_and_save(file_path)
