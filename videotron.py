# A very simple Flask Hello World app for you to get started with...
import flask
from flask import Flask, request, jsonify
import json, time, requests, copy, base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

URL = 'https://pv.alexhal.me'

@app.route('/get')
def get():
    return '1'

@app.route('/log/<ar>')
def log(ar):
    with open('videotron.json', 'rb') as f:
        vJSON = json.loads(f.read().decode('utf-8'))

    if ar == 'json':
        return jsonify(vJSON)

    rep = str(int(len(requests.get(url = URL + '/' + ar).content) == 1))

    vJSON[str(int(time.time()))] = rep

    with open('videotron.json', 'wb') as f:
        f.write(json.dumps(vJSON).encode('utf-8'))

    return rep


if False:
    with open('videotron.json', 'wb') as f:
        f.write(json.dumps({}).encode('utf-8'))