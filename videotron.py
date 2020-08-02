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
    with open('videotron_get.json', 'rb') as f:
        gJSON = json.loads(f.read().decode('utf-8'))

    with open('videotron_base.json', 'rb') as f:
        bJSON = json.loads(f.read().decode('utf-8'))

    if ar == 'gjson':
        return jsonify(gJSON)

    if ar == 'bjson':
        return jsonify(bJSON)

    bJSON[str(int(time.time()))] = '1'

    with open('videotron_base.json', 'wb') as f:
        f.write(json.dumps(bJSON).encode('utf-8'))

    rep = str(int(len(requests.get(url = URL + '/' + ar).content) == 1))

    gJSON[str(int(time.time()))] = rep

    with open('videotron_get.json', 'wb') as f:
        f.write(json.dumps(gJSON).encode('utf-8'))

    return rep


if False:
    with open('videotron_get.json', 'wb') as f:
        f.write(json.dumps({}).encode('utf-8'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
