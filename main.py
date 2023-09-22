import flask
from flask import redirect, render_template, send_file
import traceback

app = flask.Flask("bitch")

def insert(webpage):
    d = render_template("template.html", path = webpage)
    return d

@app.errorhandler(500)
def error500(e):
    trc = traceback.format_exc().replace("\n", "<br>").replace(" ", "&nbsp;")
    return f"<h3>{e}</h3><p>{trc}</p>"


@app.route("/log-in")
def what():
    return send_file("templates/log_in.html")

@app.route("/assets/<assetid>")
def getasset(assetid):
    try:
        return send_file("assets/" + assetid)
    except:
        return '', 404

@app.route("/baninfo/<banid>")
def baninfo(banid):
    return "<h1>" + banid + "</h1>"

@app.route("/")
def none():
    return insert("org.bukkit.fuckme.html"), 200

@app.route("/home")
def home():
    return redirect("/"), 301

app.run("127.0.0.1", 6942)