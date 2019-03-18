from flask import Flask , render_template, request
import food
app = Flask(__name__)
@app.route("/")
def home():
  return ("")
@app.route("/food_list")
def food_list ():
    # Get ALL Food
    all_food = food.get({})
    #render: Food + html
    # return
    return render_template("food_list.html", f_list = all_food)

@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    return render_template("food_detail.html", food = f)

@app.route("/add_food", methods= ["GET", "POST"])
def add_food():
    if request.method == "GET":
      return render_template("food_form.html")
    elif request.method == "POST":
      form = request.form
      n = form["name"]
      p = form["price"]
      food.add_food(n,p)


if __name__ == '__main__':
  app.run(port =4052,debug=True)