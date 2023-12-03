from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo_oop import Dojo


@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos/create',methods=['POST'])
def create_d():
    Dojo.create_d(request.form)
    return redirect('/dojos')

@app.route('/dojos')
def display():
    all_dojos=Dojo.get_all()
    return render_template('dojo1.html', dojo=all_dojos)

@app.route('/dojos/<int:id>')
def display_ninjas(id):
    data={'id':id}
    all_ninjas=Dojo.get_by_id(data)
    return render_template('all_ninja3.html',ninjas=all_ninjas)
    