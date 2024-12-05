from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# IBM Watson NLU configuration
ibm_api_key = 'o36koGq2Gz-M114MqRDFsbRw4CvH4kz1dhGYcJ2KVtxy'
ibm_url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/704dfba8-4c83-453c-9484-dbd5ef4dfebb'
authenticator = IAMAuthenticator(ibm_api_key)
nlu = NaturalLanguageUnderstandingV1(version='2021-08-01', authenticator=authenticator)
nlu.set_service_url(ibm_url)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')

    # Combine the text of all paragraphs for a more comprehensive summary
    full_text = ' '.join([para.get_text() for para in paragraphs])
    summary_length = 4000  # Increased length for a more comprehensive summary
    summary = full_text[:summary_length]

    return jsonify({'summary': summary})

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    response = nlu.analyze(
        text=text,
        features=Features(entities=EntitiesOptions(limit=5), keywords=KeywordsOptions(limit=5))
    ).get_result()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
