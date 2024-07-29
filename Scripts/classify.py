import joblib

def classify_text(model_path, vectorizer_path, text):
    model = joblib.load(model_path) #vortrainiertes modell laden
    vectorizer = joblib.load(vectorizer_path) #vektorisierer laden
    text_vectorized = vectorizer.transform([text]) #text zu vektor
    predicted_label = model.predict(text_vectorized) #sagt ddc aus modell und vektor voraus
    return predicted_label
