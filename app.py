from chalice import Chalice
from urlparse import urlparse
import boto3
import json

app = Chalice(app_name='sent')

@app.route('/articleScore', methods=['POST'], cors=True)
def index():
    request = app.current_request.json_body
    validArticle = []
    index = 0
    for x in request:
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        description = x['description']
        if(description is not None and len(description) > 0):
            responseDesc = comprehend.detect_sentiment(Text=description, LanguageCode='en')

        title = x['articleTitle']
        if(title is not None and len(title) > 0):
            responseTitle = comprehend.detect_sentiment(Text=title, LanguageCode='en')

        content = x['content']
        if(content is not None and len(content) > 0):
            responseContent = comprehend.detect_sentiment(Text=content, LanguageCode='en')


        if responseDesc['Sentiment'] == "NEUTRAL" or responseContent['Sentiment'] == "NEUTRAL":
            validArticle.insert(index, x)
        elif responseDesc['SentimentScore']['Neutral'] >= 0.47:
            validArticle.insert(index, x)
        elif responseTitle['SentimentScore']['Neutral'] >= 0.45:
            validArticle.insert(index, x)
        elif responseContent['SentimentScore']['Neutral'] >= 0.47:
            validArticle.insert(index, x)

        index += 1

    return json.dumps(validArticle)
