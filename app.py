# import needed libraries
import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from validate_email import validate_email
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from random import randint
import random

# initalize flask app
app = Flask(__name__)

# Define secret key and hide it
app.secret_key = os.environ.get("c!o@l#t$a5r6")

# Set database to use filesystem instead of signed cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Link Database coltar.db
db = "sqlite:///coltar.db"

# create an engine to apply on
engine = create_engine(db)

# dont let to acces some pages if the user isnt loged in
def login_required(f):
  """
  Decorate routes to require login.

  http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
  """
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
      return redirect("/")
    return f(*args, **kwargs)
  return decorated_function

@app.route("/", methods=["GET", "POST"])
def index():
  # Check if user is submitting or accesing page
  if request.method == "GET":
    # if accesing page then render it
    return render_template("index.html")
  
  else:
    # get the user and email submitted
    name = request.form.get("username")
    email = request.form.get("email")
    
    # Confirm that they're not blank
    if not name or not email:
      flash("يجب توفير اسم المتسابق وبريده الابكتروني")
      return redirect("/")
    
    # Create connection to apply on it
    connection = engine.connect()

    # See if the user logging is an admin by checking database
    parm = {"email": email, "type": "admin"}
    emails = connection.execute("SELECT COUNT(*) FROM users WHERE email = :email AND type = :type", parm).fetchone()[0]
    if emails != 0:
      # if admin than redirect to 'log admin' page
      return render_template("log.html", email=email)
    
    # Confirm that this name isnt taken before
    parm = {"name": name}
    names = connection.execute("SELECT COUNT(*) FROM users WHERE name = :name", parm).fetchone()[0]
    if names != 0:
      flash("هذا الاسم مستخدم بالفعل")
      return redirect("/")
    
    # Confirm that the email provided is valid
    if not validate_email(email):
      flash("يرجى ادراج بريجد الكتروني سليم")
      return redirect("/")
    
    # Add user to database
    parm = {"name": name, "email": email, "type": "user"}
    connection.execute("INSERT INTO users (name, email, type) VALUES (:name, :email, :type)", parm)

    # Get user id
    parm = {"name": name}
    id = connection.execute("SELECT id FROM users WHERE name = :name", parm).fetchone()
    session["user_id"] = id["id"]

    # redirect to info page
    return redirect("/info")  

@app.route("/info")
@login_required
def info():
  # Get info stored in database
  connection = engine.connect()
  s_info = connection.execute("SELECT cont FROM info").fetchall()

  # render info template and pass the info to it]
  return render_template("info.html", s_info=s_info)

@app.route("/log", methods= ["POST", "GET"])
def log():
  # Check if user is submitting or accesing page
  if request.method == "GET":
    # if accesing page then render it
    return render_template("log.html")
  
  else:
    # if submitting then get the form
    email = request.form.get("email")
    password = request.form.get("password")

    # Confirm that form isnt blank
    if not email or not password:
      flash("يجب توفير بريد المتسابق الابكتروني وكلمة السر")
      return redirect("/log")
    
    # Confirm that the email is an admin email
    connection = engine.connect()
    parm = {"email": email, "type": 'admin'}
    check = connection.execute("SELECT COUNT(*) FROM users WHERE email = :email AND type = :type", parm).fetchone()[0]
    if check == 0:
      flash("هذا البريد الكتروني ليس بريد مسؤول")
      return redirect("/")
    
    # Confirm that password is correct for admin email
    parm = {"email": email}
    check1 = connection.execute("SELECT * FROM users WHERE email = :email", parm).fetchone()
    if check_password_hash(check1["password"], password):
      # Then add admin id and redirect to administration
      session["user_id"] = check1["id"]
      return redirect("/admin")
    
    else:
      # Redirect to same page with flash message
      flash("كلمة المرو خاطئة")
      return redirect("/log")

@app.route("/admin", methods= ["POST", "GET"])
@login_required
def admin():
  # Confirm that the user is an admin
  connection = engine.connect()
  parm = {"id": session["user_id"]}
  check = connection.execute("SELECT * FROM users WHERE id = :id", parm).fetchone()
  if check["type"] != "admin":
    flash("هذا الحساب ليس حسابا مسؤولا")
    return redirect("/")

  # Check if user is submitting or accesing page
  if request.method == "GET":
    # if accesing page then render it
    return render_template("admin.html")
  
  else:
    # Get the form that are submited
    name = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    info = request.form.get("info")
    question = request.form.get("question")
    fans = request.form.get("fans")
    tan = request.form.get("tan")
    
    # Check which form submitted among the 3 forms
    if name and email and password:
      # If user was in db as type 'user' then delete it
      parm = {"email": email}
      connection.execute("DELETE FROM users WHERE email = :email", parm)
      
      # Add admin to db as admin
      parm = {"name": name, "email": email, "type": "admin", "password": generate_password_hash(password)}
      connection.execute("INSERT INTO users (name, email, type, password) VALUES (:name, :email, :type, :password)", parm)
      flash("Admin Was Succesfully Added")

      # redirect to /admin
      return redirect("/admin")
    
    elif info:
      # Insert info added into db
      parm = {"cont": info}
      connection.execute("INSERT INTO info (cont) VALUES(:cont)", parm)
      flash("Information Was Succesfully Added")

      # redirect to /admin
      return redirect("/admin")
    
    elif question and fans and tan:
      # Store False answers in one list
      mylist = []
      bas = ""
      for i in range(0, len(fans)):
        if fans[i] == '-' or fans[i] == '.':
          mylist.append(bas)
          bas = ""
        else:
          bas += fans[i]

      # Add Question to db
      parm = {"question": question, "f1": mylist[0], "f2": mylist[1], "f3": mylist[2], "t": tan}
      connection.execute("INSERT INTO questions (question, f1, f2, f3, t) VALUES(:question, :f1, :f2, :f3, :t)", parm)
      flash("The Question Was Succesfully Added")
      
      # redirect to /admin
      return redirect("/admin")
    
    else:
      # if all forms are blank then redirect to /admin
      flash("يرجى ادراج المعلومات المطلوبة")
      return redirect("/admin")

@app.route("/test", methods=["POST", "GET"])
@login_required
def test():
  # if the values of ids, index and scores arent intialized in session then initialize it
  connection = engine.connect()
  if 'values' not in session:
    session["values"] = []
  if 'i' not in session:
    session['i'] = 0
  if 'score' not in session:
    session['score'] = 0

  # Check if user is submitting or accesing page
  if request.method == "GET":
    # if accesing page and values is empty then fill it with ids of questions from db
    if not session['values']:
      ques_count = connection.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
      while len(session['values']) < 10:
        val = randint(1, ques_count)
        if val not in session['values']:
          session['values'].append(val)

    if session['i'] >= len(session['values']):  # Reset session['i'] if it exceeds the length
      session['i'] = 0
    
    # Initialize session['score'] if it doesn't exist yet
    if 'score' not in session:
      session['score'] = 0

    # get from the db the question with ids stored in db
    ques_id = session['values'][session['i']]
    parm = {"ques_id":ques_id}
    ques = connection.execute("SELECT * FROM questions WHERE ques_id = :ques_id", parm).fetchone()
    
    session['i'] += 1 # increment index by 1

    # put answers in list to be passed to test template
    mylist = [ques["f1"], ques["t"], ques["f2"], ques["f3"]]
    
    # Randomize the order of answers in list
    random.shuffle(mylist)

    # render page
    return render_template("test.html", ques=ques, mylist=mylist)
  
  else:
    # Get the answer submitted and id of question
    ques_id = request.form.get("id")
    ans = request.form.get("ans")

    # See what is the true answer for this specific question in db
    parm = {"ques_id": ques_id}
    tr_ans = connection.execute("SELECT t FROM questions WHERE ques_id = :ques_id", parm).fetchone()[0]

    # compare the answer submitted with the true answer
    if tr_ans == ans:
      # if true then increment score by 1
      session['score'] += 1
    
    # if user was asked 10 questions
    if session['i'] == 10:
      # then redirect to scores page
      return redirect("/scores")
    
    # else send to be asked another question
    return redirect("/test")

@app.route("/scores")
@login_required
def scores():
  # set res = score
  res = session.get('score')
  # set values, index and score to initial values
  session['score'] = 0
  session['i'] = 0
  session['values'] = []

  if res is None:
    res = 0
  # redirect to page in which score is shown
  return render_template("scores.html", score=res)

# Errors handlers for 404 and 500 errors
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
  return render_template("500.html"), 500

# Run app
if  __name__ == "__main__":
  app.run()