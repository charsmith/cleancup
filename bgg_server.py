import json
from bgg import Plays
from flask import Flask, Response, redirect, url_for
from datetime import date
app = Flask(__name__)

p = Plays()

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route("/plays/<name>/<mindate>")
@app.route("/plays/<name>/<mindate>/<maxdate>")
def plays(name, mindate=None, maxdate=None):
    maxdate = maxdate and maxdate or str(date.today())
    js = json.dumps(p.plays(name, mindate, maxdate))
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()
