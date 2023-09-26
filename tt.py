import json
import uuid

def gen(name):
    f = json.load(open("db/token.json"))
    c = str(uuid.uuid4()).replace("-", "")
    f[c] = name
    json.dump(f, open("db/token.js", "w"))
    return c