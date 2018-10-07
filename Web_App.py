#!/usr/bin/env python
# coding=utf-8
#I use the microframe Flask to build this Web
#The Flask's Website is flask.pocoo.org
#In order to use this script, you need to install flask as follows
#sudo apt install python-pip
#sudo pip install flask

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Initialization</h1>'       

@app.route('/input',methods=['POST','GET'])
def input_number():
    if "number" in request.form:
        msg=request.form['number']
        print(msg)
    return '''<form action="/input" method="post">
              <p>Please input the control number</p>
              <p><input name="number"></p>
              <p><button type="submit">Submit</button></p>
              </form>'''

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
#    app.run()
