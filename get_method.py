from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("form.html")



@app.route("/result")
def result():
    name = request.args.get("username")
    age = request.args.get("age")

    return f"<h1>Hello {name}, you are {age} years old</h1>"


app.run(debug=True)
