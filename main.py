from flask import Flask, jsonify, request

from analysis import Analyse

import requests

app = Flask(__name__)

@app.route("/")
def main():
    return "first route"

@app.route('/api/messages', methods=['POST'])
def add_message():
    content = request.json
    print content
    test = Analyse()
    print dir(request.json)

    test.treat_message(request.json["text"],request.json["message"])


    return jsonify(content)




if __name__ == "__main__":
    app.run()
