
import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from validate_email import validate_email
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from random import randint
import random

app = Flask(__name__)

app.secret_key = os.environ.get("c!o@l#t$a5r6")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = "sqlite:///coltar.db"

engine = create_engine(db)


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
  if request.method == "GET":
    return render_template("index.html")
  else:
    name = request.form.get("username")
    email = request.form.get("email")
    if not name or not email:
      flash("يجب توفير اسم المتسابق وبريده الابكتروني")
      return redirect("/")
    connection = engine.connect()
    parm = {"email": email, "type": "admin"}
    emails = connection.execute("SELECT COUNT(*) FROM users WHERE email = :email AND type = :type", parm).fetchone()[0]
    if emails != 0:
      return render_template("log.html", email=email)
    parm = {"name": name}
    names = connection.execute("SELECT COUNT(*) FROM users WHERE name = :name", parm).fetchone()[0]
    if names != 0:
      flash("هذا الاسم مستخدم بالفعل")
      return redirect("/")
    if not validate_email(email):
      flash("يرجى ادراج بريجد الكتروني سليم")
      return redirect("/")
    parm = {"name": name, "email": email, "type": "user"}
    connection.execute("INSERT INTO users (name, email, type) VALUES (:name, :email, :type)", parm)
    parm = {"name": name}
    id = connection.execute("SELECT id FROM users WHERE name = :name", parm).fetchone()
    session["user_id"] = id["id"]
    return redirect("/info")  

@app.route("/info")
@login_required
def info():
  connection = engine.connect()
  s_info = connection.execute("SELECT cont FROM info").fetchall()
  return render_template("info.html", s_info=s_info)

@app.route("/log", methods= ["POST", "GET"])
def log():
  if request.method == "GET":
    return render_template("log.html")
  else:
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
      flash("يجب توفير بريد المتسابق الابكتروني وكلمة السر")
      return redirect("/log")
    connection = engine.connect()
    parm = {"email": email, "type": 'admin'}
    check = connection.execute("SELECT COUNT(*) FROM users WHERE email = :email AND type = :type", parm).fetchone()[0]
    if check == 0:
      flash("هذا البريد الكتروني ليس بريد مسؤول")
      return redirect("/")
    parm = {"email": email}
    check1 = connection.execute("SELECT * FROM users WHERE email = :email", parm).fetchone()
    if check_password_hash(check1["password"], password):
      session["user_id"] = check1["id"]
      return redirect("/admin")
    else:
      flash("كلمة المرو خاطئة")
      return redirect("/log")

@app.route("/admin", methods= ["POST", "GET"])
@login_required
def admin():
  connection = engine.connect()
  parm = {"id": session["user_id"]}
  check = connection.execute("SELECT * FROM users WHERE id = :id", parm).fetchone()
  if check["type"] != "admin":
    flash("هذا الحساب ليس حسابا مسؤولا")
    return redirect("/")
  if request.method == "GET":
    return render_template("admin.html")
  else:
    name = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    info = request.form.get("info")
    question = request.form.get("question")
    fans = request.form.get("fans")
    tan = request.form.get("tan")
    if name and email and password:
      parm = {"email": email}
      connection.execute("DELETE FROM users WHERE email = :email", parm)
      parm = {"name": name, "email": email, "type": "admin", "password": generate_password_hash(password)}
      connection.execute("INSERT INTO users (name, email, type, password) VALUES (:name, :email, :type, :password)", parm)
      flash("Admin Was Succesfully Added")
      return redirect("/admin")
    elif info:
      parm = {"cont": info}
      connection.execute("INSERT INTO info (cont) VALUES(:cont)", parm)
      flash("Information Was Succesfully Added")
      return redirect("/admin")
    elif question and fans and tan:
      mylist = []
      bas = ""
      for i in range(0, len(fans)):
        if fans[i] == '-' or fans[i] == '.':
          mylist.append(bas)
          bas = ""
        else:
          bas += fans[i]
      parm = {"question": question, "f1": mylist[0], "f2": mylist[1], "f3": mylist[2], "t": tan}
      connection.execute("INSERT INTO questions (question, f1, f2, f3, t) VALUES(:question, :f1, :f2, :f3, :t)", parm)
      flash("The Question Was Succesfully Added")
      return redirect("/admin")
    else:
      flash("يرجى ادراج المعلومات المطلوبة")
      return redirect("/admin")

@app.route("/test", methods=["POST", "GET"])
@login_required
def test():
  connection = engine.connect()
  if 'values' not in session:
    session["values"] = []
  if 'i' not in session:
    session['i'] = 0
  if 'score' not in session:
    session['score'] = 0
  if request.method == "GET":
    if not session['values']:
      ques_count = connection.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
      while len(session['values']) < 10:
        val = randint(1, ques_count)
        if val not in session['values']:
          session['values'].append(val)

    if session['i'] >= len(session['values']):  # Reset session['i'] if it exceeds the length
      session['i'] = 0
    ques_id = session['values'][session['i']]
    parm = {"ques_id":ques_id}
    ques = connection.execute("SELECT * FROM questions WHERE ques_id = :ques_id", parm).fetchone()
    session['i'] += 1
    mylist = [ques["f1"], ques["t"], ques["f2"], ques["f3"]]
    random.shuffle(mylist)
    return render_template("test.html", ques=ques, mylist=mylist)
  else:
    ques_id = request.form.get("id")
    ans = request.form.get("ans")
    parm = {"ques_id": ques_id}
    tr_ans = connection.execute("SELECT t FROM questions WHERE ques_id = :ques_id", parm).fetchone()[0]
    if tr_ans == ans:
      session['score'] += 1
    if session['i'] == 10:
      return redirect("/scores")
    return redirect("/test")

@app.route("/scores")
def scores():
  return render_template("scores.html", score=session['score'])

@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
  return render_template("500.html"), 500

if  __name__ == "__main__":
  app.run()