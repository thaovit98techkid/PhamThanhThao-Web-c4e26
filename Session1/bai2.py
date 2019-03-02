from flask import Flask
app = Flask(__name__)
@app.route("/")
def a ():
    return ("")
@app.route("/<int:bmi>/<int:weight>/<int:height>")
def BMI(bmi,weight,height):
    if bmi <16:
        return ("Severely underweight")
    elif 16 <= bmi < 18.5:
        return ("Underweight")
    elif 18.5 <= bmi < 25:
        return ("Normal")
    elif 25 <= bmi < 30:
        return ("overweight")
    else :
        return ("Obese")
if __name__ == '__main__':
  app.run(port =5000,debug=True)