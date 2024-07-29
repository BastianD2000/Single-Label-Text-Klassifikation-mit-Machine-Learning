#je nachdem ob naive_bayes oder svc gewünscht, im import und bei zeile 13/14 unerwünschtes auskommentieren

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  
#from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib
import os

def train_and_save_model(X, y, model_path, vectorizer_path, vectorizer, evaluation_path): # train-test-split mit stratify, für ausgewogene verteilung der klassen
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) #20% testdaten, 42 ist zufallsstartwert für reproduzierbarkeit der aufteilung, x merkmalsmatrix, y zielwerte

    model = SVC()  
    #model = MultinomialNB()
    model.fit(X_train, y_train) #trainiert modell mit trainingsdaten

    # vorhersage
    y_pred = model.predict(X_test)

    # ergebnisse anzeigen
    report = classification_report(y_test, y_pred, output_dict=True)
    
    # formatieren der evaluierung
    formatted_report = format_classification_report(report)

    # evaluierung in datei schreiben
    with open(evaluation_path, 'w') as f:
        f.write(formatted_report)

    # modell speichern
    joblib.dump(model, model_path)

    # vektorisierer speichern
    joblib.dump(vectorizer, vectorizer_path)
    
    return model, formatted_report

def format_classification_report(report):
    lines = []
    for label, metrics in report.items():
        if isinstance(metrics, dict):
            lines.append(f"Label: {label}")
            for metric, value in metrics.items():
                lines.append(f"  {metric}: {value:.2f}")
            lines.append("")  
        else:
            lines.append(f"{label}: {metrics:.2f}")
    return "\n".join(lines)
