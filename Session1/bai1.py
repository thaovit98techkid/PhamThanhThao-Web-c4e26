import os
from flask import Flask,redirect
app = Flask(__name__)
@app.route("/")
def a ():
    return ("")
me = [
    "Pham Thanh Thao",
    'TechKid',
    'Thang Long University',
    'read book, photograbpher, football',
     'Y',
    ]
@app.route("/aboute-me")
def my_infor ():
    
    return str(me)
@app.route ("/school")
def school ():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run( host='127.0.0.1',port = 5000,debug=True)