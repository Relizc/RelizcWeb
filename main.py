import flask
from flask import redirect, render_template, send_file

app = flask.Flask("bitch")

@app.route("/assets/<assetid>")
def getasset(assetid):
    try:
        return send_file("assets/" + assetid)
    except:
        return '', 404nb

@app.route("/baninfo/<banid>")
def baninfo(banid):
    return "<h1>" + banid + "</h1>"

@app.route("/")
def none():
    return render_template("home.html"), 200

app.run("127.0.0.1", 6942)