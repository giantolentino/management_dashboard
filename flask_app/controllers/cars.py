from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.car import Car
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
  if 'user_id' not in session:
      return redirect('/logout')
  data ={
      'id': session['user_id']
  }
  user = User.get_by_id(data)
  cars = Car.get_all()
  return render_template("dashboard.html", user=user, cars=cars)

@app.route('/add')
def add():
  data ={
      'id': session['user_id']
  }
  return render_template("add.html", user=User.get_by_id(data))

@app.route('/add/car',methods=['POST'])
def add_car():
  if Car.validate_car(request.form):
        Car.save(request.form)
        return redirect('/dashboard')
  return redirect('/add')

@app.route('/destroy/car/<int:id>')
def destroy(id):
  data ={
      'id': id
  }
  Car.destroy(data)
  return redirect('/dashboard')

@app.route('/car/<int:id>')
def show_car(id):
  data = {
      "id": id
  }
  car = Car.get_car_by_id(data)
  return render_template('car.html', car=car)

@app.route('/edit/car/<int:id>')
def edit(id):
  data ={ 
      "id":id
  }
  return render_template("edit.html",car=Car.get_car_by_id(data))

@app.route('/update/car',methods=['POST'])
def update():
  if Car.validate_car(request.form):
        Car.update(request.form)
        return redirect('/dashboard')
  return redirect(request.referrer)