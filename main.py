from flask import Flask, jsonify, request

from analysis import Analyse

import requests

import sqlite3
from flask import g

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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

    cur.execute("SELECT * FROM mooding");

    for row in cur :
        print row


    db.close()


    return jsonify(content)




if __name__ == "__main__":
    app.run()
