from pymongo import MongoClient 
from datetime import datetime, date
from werkzeug.utils import secure_filename
import os
from flask import Flask, flash, request, redirect, url_for
from flask import *
import pandas as pd
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

try:
    client = MongoClient("mongodb+srv://codefundo:codefundo@cluster0-qx5uu.azure.mongodb.net/test?retryWrites=true") 
    print("connection successfull!")

except:
    print("connection not established")

db=client.get_database('codefundo')
records=db.voterIds #collection or table
print(records.count_documents({}))

@app.route('/api/v1/login', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def login():
    if(request.method=='POST'):
        if(request.is_json):
            voterid=request.json['voter_id']
            pwd=request.json['password']
        else:
            recieved=json.loads(request.data)
            voterid=recieved['voter_id']
            pwd=recieved['password']
        x=list(records.find({ "voter_id": voterid, "password": pwd }))
        if(len(x)==0):
            print("empty")
            if(request.is_json):
                return jsonify({}), 400
            else:
                return jsonify(status = "User Doesn't exist or Wrong password")
        else:
            print(x)
        if(request.is_json):
            return jsonify({}),200
        return jsonify(status = "Successful")
    else:
        return jsonify({}),405


if(__name__=="__main__"):
    app.run(debug=True)