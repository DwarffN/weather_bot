import json
import requests
from flask import Flask
from flask import jsonify
from flask import request
from app import token_inf
from app import weather as weth


app = Flask(__name__)
token = token_inf.token
URL = 'https://api.telegram.org/bot' + token + '/'


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def send_message(chat_id, text='Wait please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        weather = weth.find_weather(str(message).lower())
        send_message(chat_id, weather)
        return jsonify(r)

    return '<h1>Hello Bot</h1>'
    # https://api.telegram.org/bot753140004:AAFdIf3sQWuWEGrfEMAb1cRm8-4XqMKZhq4/setWebhook?url=https://52b01bbf.ngrok.io


if __name__ == '__main__':
    print('Runed')
    app.run()
