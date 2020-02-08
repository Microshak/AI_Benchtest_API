import time

import redis
from flask import Flask, jsonify, request, session
from datetime import timedelta
import json

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)




@app.route('/device/<apikey>', methods=['POST']) 
def predict(apikey):
    if(apikey != "152246f8-c2cc-4ab3-b4b9-529ab36ec5f6"):
        return "nope", 401
    data = request.json
   
    dat =jsonify(data)

    r.setex(request.json['name'], timedelta(minutes=15), value=json.dumps(data) )
    
    return dat


@app.route('/')
def hello():

    ret = []

    for key in r.scan_iter():
        ret.append(json.loads(r.get(key)))
        

    return jsonify(ret)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)