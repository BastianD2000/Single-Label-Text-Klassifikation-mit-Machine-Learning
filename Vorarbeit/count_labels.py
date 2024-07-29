#wegen stratify führen ddc die nur einmal vorkommen zu fehlern, jede muss mindestens zweimal vorkommen, das hiermit prüfen
import os
from collections import defaultdict, Counter

def count_classes(base_dir):
    class_counter = Counter()
    class_folders = defaultdict(list)
    
    # durchlaufe alle unterordner im überordner
    for subdir in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir)
        if os.path.isdir(subdir_path):
            ddc_file_path = os.path.join(subdir_path, 'ddc_groups.txt')
            
            # überprüfen, ob die datei existiert und nicht leer ist
            if os.path.isfile(ddc_file_path) and os.path.getsize(ddc_file_path) > 0:
                with open(ddc_file_path, 'r') as file:
                    first_class = file.readline().strip()
                    if first_class:
                        class_counter[first_class] += 1
                        class_folders[first_class].append(subdir)
    
    # ausgabe der klassen, die nur einmal vorkommen
    print('Klassen, die nur einmal vorkommen:')
    for cls, count in class_counter.items():
        if count == 1:
            folder = class_folders[cls][0]
            print(f'Klasse: {cls}, Unterordner: {folder}')

# aufruf
base_directory = 'dissertations'
count_classes(base_directory)
