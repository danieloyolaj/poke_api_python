from flask import Flask, render_template, url_for
from flask_api import status
import requests

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('index.html')

@app.route("/poke")
def poke():
  return render_template('poke.html')

@app.route("/status")
def status():
  return render_template('status.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000, debug=True)