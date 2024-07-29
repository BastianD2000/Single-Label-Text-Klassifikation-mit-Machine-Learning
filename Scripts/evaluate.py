from sklearn.metrics import classification_report
import joblib

def evaluate_model(model_path, X_test, y_test):
    model = joblib.load(model_path) #lädt vortrainiertes modell
    y_pred = model.predict(X_test) #sagt labels für testdaten voraus
    print(classification_report(y_test, y_pred)) #erstellt evaluation
