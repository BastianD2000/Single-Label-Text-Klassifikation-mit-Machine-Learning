#pdfs und ddc in txtfiles aus xml ziehen und in ordnerstruktur speichern, prozess dauert und benötigt 40gb speicher, vorsicht

"""""

import os
import requests
from lxml import etree

# pfad zur xml-datei
xml_file_path = 'C:/Users/admin/Desktop/Studium/4. Semester/Machine Learning/Projekt/export_tuprints_XML.xml'

# verzeichnis, in dem die dissertationen gespeichert werden sollen
output_directory = 'dissertations'

# xml-datei als bytes einlesen
with open(xml_file_path, 'rb') as xml_file:
    xml_content = xml_file.read()

# xml parsen
tree = etree.fromstring(xml_content)

# xml-namespace
namespace = {'ns': 'http://eprints.org/ep2/data/2.0'}

# eprint-knoten finden
eprints = tree.findall('ns:eprint', namespaces=namespace)

# funktion zum erstellen von ordnern und speichern von dateien
def save_dissertation(eprint_id, pdf_url, ddc_groups):
    # ordner für dissertation erstellen
    dir_path = os.path.join(output_directory, eprint_id)
    os.makedirs(dir_path, exist_ok=True)

    # pdf herunterladen und speichern
    if pdf_url:
        pdf_response = requests.get(pdf_url)
        pdf_filename = os.path.join(dir_path, pdf_url.split('/')[-1])
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

    # ddc-gruppen in textdatei schreiben
    ddc_filename = os.path.join(dir_path, 'ddc_groups.txt')
    with open(ddc_filename, 'w', encoding='utf-8') as ddc_file:
        ddc_file.write('\n'.join(ddc_groups))

# jede dissertation verarbeiten
for eprint in eprints:
    eprint_id = eprint.get('id').split('/')[-1]
    pdf_element = eprint.find('.//ns:document/ns:files/ns:file[ns:mime_type="application/pdf"]/ns:url', namespaces=namespace)
    pdf_url = pdf_element.text if pdf_element is not None else None
    ddc_groups = [item.text for item in eprint.findall('.//ns:ddc_dnb/ns:item', namespaces=namespace)]
    
    save_dissertation(eprint_id, pdf_url, ddc_groups)

    
"""""