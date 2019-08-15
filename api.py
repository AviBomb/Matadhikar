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
record_voterId=db.voterIds
record_candidates=db.candidates
record_party=db.parties

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
        x=list(record_voterId.find({ "voter_id": voterid, "password": pwd }))
        if(len(x)==0):
            print("empty")
            if(request.is_json):
                return jsonify({}),400
            else:
                return jsonify(status = "User Doesn't exist or Wrong password"),400
        else:
            print(x)
        if(request.is_json):
            return jsonify({}),200
        return jsonify(status = "Successful"),200
    else:
        return jsonify({}),405

@app.route('/api/v1/candidates/<string:district_num>/<string:ward_num>', methods=['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def get_candidates(district_num,ward_num):
    if(request.method=='GET'):
        print(district_num)
        print(ward_num)
        x=list(record_candidates.find({"Ward number":ward_num,"District number":district_num}))
        if(len(x)==0):
            print("empty")
            if(request.is_json):
                return jsonify({}),400
            else:
                return jsonify(status = "Ward number or District number is wrong")
        else:
            for i in x:
                i["_id"]=str(i["_id"])
            if(request.is_json):
                return jsonify(x),200
            else:
                return jsonify(x),200
    else:
        return jsonify({}),405

@app.route('/api/v1/forgotpassword', methods =['GET','POST','DELETE','PUT'])
@cross_origin(supports_credentials=True)
def forgot_password():
    if(request.method=='POST'):
        if(request.is_json):
            voterid=request.json['voter_id']
            ph_no=request.json['ph_no']
        else:
            recieved=json.loads(request.data)
            voterid=recieved['voter_id']
            ph_no=recieved['ph_no']
        x=list(record_voterId.find({ "voter_id": voterid, "ph_no": ph_no }))
        if(len(x)==0):
            print("empty")
            if(request.is_json):
                return jsonify({}), 400
            else:
                return jsonify(status = "User Doesn't exist or Wrong phone number")
        else:
            print(x)
        if(request.is_json):
            return jsonify({}),200
        return jsonify(status = "Successful")
    else:
        return jsonify({}),405

if(__name__=="__main__"):
    app.run(debug=True)