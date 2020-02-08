import time

import redis
from flask import Flask, jsonify, request, session
from datetime import timedelta
import json

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)




@app.route('/device', methods=['POST']) 
def predict():
    data = request.json
    print('jejjjjjjjjj')
    #name = data['name']
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