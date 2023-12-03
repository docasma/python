from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.ninja_oop import Ninja
from flask_app.models.dojo_oop import Dojo


@app.route('/ninjas/create',methods=['POST'])
def create_n():
    data=request.form
    Ninja.create_n(data)
    return redirect('/')

@app.route('/ninjas')  
def add_ninja():
    get=Dojo.get_all()
    return render_template('new_ninja2.html',dojos=get)
 