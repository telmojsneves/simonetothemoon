from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return "first route"

if __name__ == "__main__":
    app.run()
