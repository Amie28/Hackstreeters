from time import sleep
from flask import Flask, send_from_directory,request
#from flask_cors import CORS
import os
import json
from eye import *



app=Flask(__name__,static_folder='build',static_url_path='/')

@app.route('/',methods=['GET'])
def index():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/coffee',methods=['GET'])
def index_coffee():
    return send_from_directory(app.static_folder,'index_coffee.html')

@app.route('/api/runimage_beer/',methods=['GET'])
def runimage_beer():
    print('Button clicked')
    import gad
    age, gender = gad.get_data()
    print(age,gender)
    import videoTester
    sentiment = videoTester.get_data()
    print(sentiment)
    if(sentiment=='sad'):
        ad = 'Ads/Beer_sad.png'
    elif(sentiment=='happy'):
        ad='Ads/Beer_happy.png'
    else:
        ad='Ads/Beer_neutral.png'
    return json.dumps({'ad': ad,'age':age,'sentiment':sentiment,'gender':gender})

@app.route('/api/runimage_coffee/',methods=['GET'])
def runimage_coffee():
    print('Button clicked')
    import gad
    age, gender = gad.get_data()
    print(age,gender)
    import videoTester
    sentiment = videoTester.get_data()
    print(sentiment)
    if(age == '0-3' or age =='4-9' or age == '10-16' or age == '17-25' or age == '26-35'):
        ad='Ads/Coffee_lessthan_30.png'
    if(age == '36-43' or age == '44-53' or age == '54-100'):
        ad='Ads/Coffee_greaterthan_30.png'
    return json.dumps({'ad': ad,'age':age,'sentiment':sentiment,'gender':gender})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6000)