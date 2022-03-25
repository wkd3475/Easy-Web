from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

li_list = []

@app.route('/', methods=['GET'])
def index():
    return {'hello': 'world!'}

@app.route('/boards', methods=['GET', 'POST'])
def boards():
    if request.method == 'GET':
        return {'boards': li_list}
    else:
        li_list.append(request.get_json()['board'])
        return {}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)