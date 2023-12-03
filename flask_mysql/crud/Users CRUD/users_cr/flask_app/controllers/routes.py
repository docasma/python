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

#routes to create
@app.route("/user/new")
def new_user():
    return render_template("create.html")

@app.route("/user/create", methods=["POST"])
def create():
    print(request.form)  
    User.insert_user(request.form)
    return redirect("/users")

#routes to update
@app.route("/user/<int:id>/edit")
def update(id):
    data={"id":id}
    user=User.get_by_id(data)
    return render_template("update.html", user=user)

@app.route("/update",methods=["POST"])
def to_update():
    data=request.form
    User.update(data)
    return redirect("/users")

@app.route("/user/<int:id>")
def show(id):
    data={"id":id}
    return render_template("show.html", user=User.get_by_id(data))

#routes to delete
@app.route("/user/<int:id>/delete")
def delete(id):
    data={"id":id}
    User.delete(data)
    return redirect("/users")  


