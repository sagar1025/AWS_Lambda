from chalice import Chalice
from urlparse import urlparse
import boto3
import json

app = Chalice(app_name='sent')

@app.route('/articleScore', methods=['POST'])
def index():
    request = app.current_request.json_body
    score = 0.0
    validArticle = {}
    index = 0
    for x in request['articles']:
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        text = x['title']
        response = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
        print(response)
        jsonresp = json.loads(response)

        print(jsonresp['Sentiment'])
        print(jsonresp['SentimentScore']['Positive'])
        if jsonresp['Sentiment'] == "NEUTRAL":
            validArticle[index] = x
        elif jsonresp['SentimentScore']['Neutral'] >= 0.45:
            validArticle[index] = x

        index += 1

    return json.dumps(validArticle)
