from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.property import Property
from flask_app.models.user import User

@app.route('/add/property')
def add():
  data ={
      'id': session['user_id']
  }
  return render_template("add_property.html")

@app.route('/add/property/property',methods=['POST'])
def add_property():
  property.save(request.form)
  return redirect('/dashboard')
  # if property.validate_property(request.form):
  #       property.save(request.form)
  #       return redirect('/dashboard')
  # return redirect('/add')

# @app.route('/destroy/car/<int:id>')
# def destroy(id):
#   data ={
#       'id': id
#   }
#   Car.destroy(data)
#   return redirect('/dashboard')

# @app.route('/car/<int:id>')
# def show_car(id):
#   data = {
#       "id": id
#   }
#   car = Car.get_car_by_id(data)
#   return render_template('car.html', car=car)

# @app.route('/edit/car/<int:id>')
# def edit(id):
#   data ={ 
#       "id":id
#   }
#   return render_template("edit.html",car=Car.get_car_by_id(data))

# @app.route('/update/car',methods=['POST'])
# def update():
#   if Car.validate_car(request.form):
#         Car.update(request.form)
#         return redirect('/dashboard')
#   return redirect(request.referrer)