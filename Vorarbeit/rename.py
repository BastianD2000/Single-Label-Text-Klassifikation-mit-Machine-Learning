#benennt alle txtfiles der dissertationen zu text.txt

import os

def umbenennen(pfad):
  
  for dateiname in os.listdir(pfad):
    vollständiger_pfad = os.path.join(pfad, dateiname)
    if os.path.isfile(vollständiger_pfad) and dateiname != "ddc_groups.txt" and not dateiname.endswith(".pdf"):
      neue_endung = ".txt" if dateiname.endswith(".txt") else ""
      neuer_dateiname = f"text{neue_endung}"
      os.rename(vollständiger_pfad, os.path.join(pfad, neuer_dateiname))

    elif os.path.isdir(vollständiger_pfad):
      umbenennen(vollständiger_pfad)

if __name__ == "__main__":
  pfad = "dissertations"  
  umbenennen(pfad)

