from flask import Flask, request, jsonify
from Exceptions import ProcessErrorException

app = Flask(__name__)


@app.route('/')
def base():
    return "Hello World!!"


@app.route('/parser', methods=['POST'])
def parse_input():
    try:
        req = request.get_json()
        ff = req.get("FirstFrameNumber")
        lf = req.get("LastFrameNumber")
        if not ff or not lf or not req.get("Filename"):
            raise ProcessErrorException("Input data not specified")
        resp = dict()
        resp["FirstFrame"] = req.get("Filename").replace("%07d", ff)
        resp["LastFrame"] = req.get("Filename").replace("%07d", lf)
        return resp, 200

    except ProcessErrorException as ex:
        return jsonify({"error": ex.err_message}), 403

    except Exception as ex:
        return jsonify({"error": "Internal Server Error"}), 500
