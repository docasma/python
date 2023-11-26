#import the app from __init__ from flask_app
from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.user_oop import User

@app.route("/")
def home():
    return redirect("/users")

@app.route("/users")
def users():
    all_users= User.get_all()
    return render_template("users.html", users=all_users)

@app.route("/user/new")
def new_user():
    return render_template("create.html")

@app.route("/user/create", methods=["POST"])
def create():
    print(request.form)  
    User.insert_user(request.form)
    return redirect("/users")


