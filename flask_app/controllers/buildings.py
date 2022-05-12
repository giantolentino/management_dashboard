from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.building import Building
from flask_app.models.user import User

@app.route('/buildings')
def buildings():
  buildings = Building.get_all()
  return render_template("buildings.html", buildings=buildings)

@app.route('/add/building')
def add():
  data ={
      'id': session['user_id']
  }
  return render_template("add_building.html")

@app.route('/add/building/building',methods=['POST'])
def add_building():
  Building.save(request.form)
  return redirect('/dashboard')
  # if property.validate_property(request.form):
  #       property.save(request.form)
  #       return redirect('/dashboard')
  # return redirect('/add')

@app.route('/destroy/building/<int:id>')
def destroy(id):
  data ={
      'id': id
  }
  Building.destroy(data)
  return redirect('/buildings')

@app.route('/building/<int:id>')
def show_building(id):
  data = {
      "id": id
  }
  building = Building.get_building_by_id(data)
  return render_template('show_building.html', building=building)

@app.route('/edit/building/<int:id>')
def edit(id):
  data ={ 
      "id":id
  }
  return render_template("edit_building.html",building=Building.get_building_by_id(data))

@app.route('/update/building',methods=['POST'])
def update():
  Building.update(request.form)
  return redirect('/buildings')
  # if Building.validate_building(request.form):
  #       Building.update(request.form)
  #       return redirect('/buildings')
  # return redirect(request.referrer)