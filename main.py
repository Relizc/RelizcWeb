import flask
from flask import redirect, render_template, send_file, request, jsonify
import traceback
import uuid
import time
import sha256
import json
import tt

app = flask.Flask("bitch")

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

def uuid4():
    return str(uuid.uuid4()).replace("-", "")

def fail(information, **kwargs):
    return jsonify({"error": kwargs.get("status", 500),
    "dump": uuid4(), "ts": int(round(time.time())),
    "message": information,
    "code": kwargs.get("code", 0)}), kwargs.get("status", 500)

def standard(message, **kwargs):
    return jsonify({"message": message, "status": kwargs.get("status", 200),
    "code": 0}), kwargs.get("status", 200)


def insert(webpage):
    d = render_template("template.html", path = webpage + "/index.html", additional_source = webpage + "/header.html")
    return d

@app.errorhandler(500)
def error500(e):
    trc = traceback.format_exc().replace("\n", "<br>").replace(" ", "&nbsp;")
    return f"<h3>{e}</h3><p>{trc}</p>", 500


@app.route("/log-in")
def what():
    return insert("login")

@app.route("/assets/<assetid>")
def getasset(assetid):
    print(assetid)
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

@app.route("/api/auth")
def login():
    usr = request.headers.get("username", None)
    psw = request.headers.get("password", None)
    psw = sha256.sha_256(psw)
    print(usr, psw)
    f = json.load(open("db/users.json"))
    print(f[usr.lower()], psw)
    print(psw)
    print(f[usr.lower()] == psw)
    try:
        if f[usr.lower()]["password"] != psw:
            return fail("Incorrect username or password.", status=401, code=47099)
    except KeyError:
        return fail("Incorrect username or password.", status=401, code=47029)
    
    tok = tt.gen(usr)

    return standard(tok)

@app.route("/home")
def home():
    return redirect("/"), 301


app.run("127.0.0.1", 6942)