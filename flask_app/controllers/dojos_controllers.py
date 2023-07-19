from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


# All my routes go in here now  ..... Follow for all routes format---> table_name/id/actions

@app.route('/')  #This is the home route for my page
@app.route('/dojos')  #The "@" decorater associates this route with the function immediately following
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template("dojo_page.html", all_dojos=all_dojos)  # this is the route for my main page "Dojo Page"


@app.route('/dojos/create', methods=['POST'])  #create a new dojo when they login
def create_dojo():
    print("Request form", request.form)
    Dojo.create(request.form)
    return redirect('/dojos')  #needs to redirect to dojos


@app.route('/dojos/<int:id>/view') #only asking to get one dojo view link
def view_one_dojo(id):
    data = {
        'id': id
    }
    one_dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo_show.html', one_dojo=one_dojo)
