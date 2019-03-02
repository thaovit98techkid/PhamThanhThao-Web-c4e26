from flask import Flask
app = Flask(__name__)
@app.route("/")
def a ():
    return ("")
Users ={
    "Thao" : 
            {
                "name :  Pham Thanh Thao",
                "age : 23",
                "status : Khong con doc than",
            },
    "Minh" : 
            {
                 "name :  Nguyen Duc Minh",
                "age : 23",
                "status : Khong con doc than",
                
            },
    "Linh" : {
                "name :  Nguyen Tung Linh",
                "age : 23",
                "status : Khong con doc than",

            }
    

}
@app.route("/user")
def user ():
    return ("")

@app.route ("/<username>")
def user_name (username):
    a = Users["Thao"] 
    b = Users["Minh"]
    c = Users["Linh"]
    if username == "Thao":
        return str(a)
    elif username == "Minh":
        return str(b)
    elif username == "Linh":
        return str(c)
if __name__ == "__main__":
    app.run (port=5000, debug = True)
