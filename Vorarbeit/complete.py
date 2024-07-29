#prüfen ob zu jedem text extrahierter text und ddc vorhanden sind
import os
import shutil

def delete_incomplete_folders(base_dir):
    incomplete_folders = []
    # durchlaufe alle unterordner im überordner
    for subdir in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir)
        if os.path.isdir(subdir_path):
            # pfade zu den dateien in jedem unterordner
            text_file_path = os.path.join(subdir_path, 'text.txt')
            ddc_file_path = os.path.join(subdir_path, 'ddc_groups.txt')

            # überprüfen, ob beide dateien existieren und nicht leer sind
            if not os.path.isfile(text_file_path) or not os.path.isfile(ddc_file_path):
                incomplete_folders.append(subdir_path)
            elif os.path.getsize(text_file_path) == 0 or os.path.getsize(ddc_file_path) == 0:
                incomplete_folders.append(subdir_path)
    
    # löschen der unterordner mit unvollständigen daten
    for folder in incomplete_folders:
        shutil.rmtree(folder)
        print(f'Gelöscht: {folder}')

# aufruf
base_directory = 'dissertations'
delete_incomplete_folders(base_directory)
