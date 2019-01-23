from chalice import Chalice
from urlparse import urlparse
import boto3
import json

app = Chalice(app_name='sent')

@app.route('/articleScore', methods=['POST'], cors=True)
def index():
    request = app.current_request.json_body
    score = 0.0
    validArticle = {}
    index = 0
    for x in request['articles']:
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        description = x['description']
        response = comprehend.detect_sentiment(Text=description, LanguageCode='en')

        #print(response['Sentiment'])
        #print(response['SentimentScore']['Positive'])
        if response['Sentiment'] == "NEUTRAL":
            validArticle[index] = x
        elif response['SentimentScore']['Neutral'] >= 0.48:
            validArticle[index] = x

        index += 1

    return json.dumps(validArticle)
