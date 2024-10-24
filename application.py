from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

application = Flask(__name__)

def load_model():
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    
    return loaded_model, vectorizer

loaded_model, vectorizer = load_model()

@application.route('/')
def home():
    return "Fake News Detection API is running!"

@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news_text = data.get('text', '')

    if not news_text:
        return jsonify({'error': 'No text provided'}), 400

    prediction = loaded_model.predict(vectorizer.transform([news_text]))[0]

    result = 'Fake News' if prediction == 1 else 'Real News'

    return jsonify({'prediction': result})

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
