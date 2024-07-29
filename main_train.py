#hauptdatei für das trainieren und speichern des modells, ruft funktionen zum laden der daten, vektorisieren der texte und training auf

from Scripts.load_data import load_data
from Scripts.preprocess import preprocess_texts
from Scripts.training import train_and_save_model


base_path = 'dissertations' #ordner mit trainings-/testdaten, pro text ein unterordner mit pdf + txtfile mit ddc 
model_path = 'Projekt/ML/models/ddc_model.pkl'
vectorizer_path = 'Projekt/ML/models/vectorizer.pkl'
evaluation_path = 'Projekt/ML/Evaluation/evaluation.txt'

# daten laden
texts, labels = load_data(base_path)

# überprüfen, ob daten geladen wurden
if not texts or not labels:
    print("No data found. Please check your dataset directory.")
else:
    # texte vektorisieren
    X, vectorizer = preprocess_texts(texts)

    # modell trainieren, evaluieren und speichern
    model, report = train_and_save_model(X, labels, model_path, vectorizer_path, vectorizer, evaluation_path)

    print(f"Model saved to {model_path}")
    print(f"Vectorizer saved to {vectorizer_path}")
    print(f"Classification report:\n{report}")