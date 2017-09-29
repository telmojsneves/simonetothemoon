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

    test.treat_message(request.json["text"],request.json["timestamp"])

    return jsonify(content)


def switch(x):
	if x<0.25:
		return "musica1"
	elif x<0.50:
		return "musica2"
	elif x<0.75:
		return "musica3"
	else:
		return "musica4"

@app.route('/api/mood', methods=['GET'])
def get_mood():
	db = get_db()

	cur = db.cursor()

	cur.execute('SELECT * FROM mooding ORDER BY id DESC LIMIT 1')

	for row in cur:
		music_name = switch(row)

	db.close()
	return music_name


if __name__ == "__main__":
    app.run()
