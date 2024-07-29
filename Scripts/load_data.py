import os

def load_data(base_path):
    texts = []
    labels = []
    
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            text_file = os.path.join(folder_path, 'text.txt')
            label_file = os.path.join(folder_path, 'ddc_groups.txt')
            
            # überprüfen, ob die text.txt datei existiert
            if not os.path.exists(text_file):
                print(f"Warning: {text_file} does not exist, skipping this folder.")
                continue
            
            # überprüfen, ob die label.txt datei existiert
            if not os.path.exists(label_file):
                print(f"Warning: {label_file} does not exist, skipping this folder.")
                continue

            # überprüfen, ob die label.txt datei leer ist
            if os.path.getsize(label_file) == 0:
                print(f"Warning: {label_file} is empty, skipping this folder.")
                continue
            
            # öffnen der  text datei mit UTF-8 kodierung
            with open(text_file, 'r', encoding='utf-8') as tf:
                text = tf.read()
                
            # öffnen der label datei mit UTF-8 kodierung
            with open(label_file, 'r', encoding='utf-8') as lf:
                label_lines = lf.read().strip().split('\n')
                label = label_lines[0]
                
            texts.append(text)
            labels.append(label)
    
    return texts, labels
