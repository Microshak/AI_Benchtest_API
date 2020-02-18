import time

import redis
from flask import Flask, jsonify, request, session
from datetime import timedelta
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
dev = redis.Redis(host='redis', port=6379, db=0)
cam = redis.Redis(host='redis', port=6379, db=1)

@app.route('/device', methods=['POST']) 
def set_device():
    data = request.json
    dat =jsonify(data)
    dev.setex(request.json['host_name'], timedelta(minutes=15), value=json.dumps(data) )
    return dat

@app.route('/device', methods=['GET']) 
def get_device():
    ret = []

    for key in dev.scan_iter():
        ret.append(json.loads(dev.get(key)))
    return jsonify(ret)


@app.route('/cam', methods=['POST']) 
def set_cam():
    data = request.json
    dat =jsonify(data)
    cam.setex(request.json['host_name'], timedelta(minutes=15), value=json.dumps(data) )
    return dat

@app.route('/cam', methods=['GET']) 
def get_cam():
    ret = []
    for key in cam.scan_iter():
        ret.append(json.loads(cam.get(key)))
    return jsonify(ret)



@app.route('/')
def hello():

    ret = []

    for key in dev.scan_iter():
        ret.append(json.loads(dev.get(key)))
        

    return jsonify(ret)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)