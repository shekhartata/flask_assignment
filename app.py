from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def base():
    return "Hello World!!"


@app.route('/parser', methods=['POST'])
def parse_input():
    req = request.get_json()
    ff = req.get("FirstFrameNumber")
    lf = req.get("LastFrameNumber")
    resp = dict()
    resp["FirstFrame"] = req.get("Filename").replace("%07d", ff)
    resp["LastFrame"] = req.get("Filename").replace("%07d", lf)
    return resp, 200
