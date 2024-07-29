from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_texts(texts):
    vectorizer = TfidfVectorizer(stop_words='english') #erstellt tf-idf-vektorisierer unter berücksichtigung englischer stoppwörter
    X = vectorizer.fit_transform(texts) #passt vektorisierer an texte an und transformiert texte in tf-idf-vektoren
    return X, vectorizer #gibt vektoren und vektorisierer zurück
