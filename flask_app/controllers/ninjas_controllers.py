from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo



# All my routes go in here now..... Follow for all routes format---> table_name/id/actions

@app.route('/')  #This is the home route for my page
@app.route('/ninjas')  #The "@" decorater associates this route with the function immediately following
def all_ninjas():
    all_ninjas = Ninja.get_all()
    return render_template("dojo_page.html", all_ninjas=all_ninjas)  # this is the route for my main page



@app.route('/ninjas/new')   #the route to display the new ninja form
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)


@app.route('/ninjas/create', methods=['POST'])  #create a new ninja when they login
def create_ninja():
    print("Request form", request.form)
    Ninja.create(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}/view')
