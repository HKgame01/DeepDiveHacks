from flask import Blueprint, flash, render_template, request, Flask
import cohere
from mycohere import get, make

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST']) 
def home():   
  return render_template("home.html")

@app.route('/result')
def result():
  return render_template("result.html")



@app.route('/submit')
def submit():
  return render_template("submit.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
