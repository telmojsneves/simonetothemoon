from flask import Flask, jsonify, request

from analysis import Analyse

import requests

import sqlite3
from flask import g

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import unicodedata
import ast

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

DATABASE = 'database.db'


class Mooding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(128))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def main():
    return "first route"

@app.route('/api/messages', methods=['POST'])
def add_message():

    db = get_db()
    cur = db.cursor()

    print cur
    content = request.json

    test = Analyse()

    mood = test.treat_message(request.json["text"],request.json["timestamp"])

    cur.execute("INSERT INTO mooding (mood) VALUES (?)", (mood,))

    db.commit()


    db.close()

    return jsonify(content)


def switch(tuple_values):
	temp = unicodedata.normalize('NFKD', tuple_values[1]).encode('ascii','ignore')
	dic = ast.literal_eval(temp)

	x = dic["documents"][0]["score"]

	#return str(x)
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
