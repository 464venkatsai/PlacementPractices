from flask import Flask , jsonify
import requests
from flask_cors import CORS


# Initializing flask api
app = Flask(__name__)
CORS(app)


# Making a path and taking the topic
@app.route('/newapi/<topic>')
def get_news(topic):
    api_key = '8e610ab76bd3466a9eb601b9e5b838c8'
    data = requests.get(f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}').json()
    json_content = jsonify(data)
    return json_content

if __name__ == '__main__':
    app.run(debug=True)