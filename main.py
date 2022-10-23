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

@app.route('/guess', methods=['GET', 'POST'])
def guess():
  co = cohere.Client('4FqDzcvsQz5KGd4E8plG1boeLod3qsEN1Nsk5n6h')
  ques_searched = co.generate(
  model='large',
  prompt='final',
  max_tokens=50,
  temperature=0.75,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[" "],
  return_likelihoods='NONE')
  image_searched = get(ques_searched)
  return render_template("guess.html",ques_searched,image_searched)

@app.route('/quiz')
def quiz():
  co = cohere.Client('4FqDzcvsQz5KGd4E8plG1boeLod3qsEN1Nsk5n6h')
  quiz_ques = co.generate(
  model='large',
  prompt='final',
  max_tokens=50,
  temperature=0.75,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[" "],
  return_likelihoods='NONE')
  op1 = make(quiz_ques)
  op2 = make(quiz_ques)
  op3 = make(quiz_ques)
  op4 = make(quiz_ques)
  return render_template("quiz.html",op1,op2,op3,op4,quiz_ques)


@app.route('/submit')
def submit():
  return render_template("submit.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
