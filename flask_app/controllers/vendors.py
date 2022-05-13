from datetime import date
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.vendor import Vendor
from flask_app.models.user import User

@app.route('/vendors')
def vendors():
  vendors = Vendor.get_all()
  return render_template("vendors.html", vendors=vendors)

@app.route('/add/vendor')
def add_vendor():
  data ={
      'id': session['user_id']
  }
  return render_template("add_vendor.html")

@app.route('/register/vendor',methods=['POST'])
def submit_vendor():
  Vendor.save(request.form)
  return redirect('/dashboard')
  # if property.validate_property(request.form):
  #       property.save(request.form)
  #       return redirect('/dashboard')
  # return redirect('/add')

@app.route('/destroy/vendor/<int:id>')
def delete_vendor(id):
  data ={
      'id': id
  }
  Vendor.destroy_vendor(data)
  return redirect('/vendors')

@app.route('/vendor/<int:id>')
def show_vendor(id):
  data = {
      "id": id
  }
  vendor = Vendor.get_vendor_by_id(data)
  return render_template('show_vendor.html', vendor=vendor)

@app.route('/edit/vendor/<int:id>')
def edit_vendor(id):
  data ={ 
      "id":id
  }
  return render_template("edit_vendor.html",vendor=Vendor.get_vendor_by_id(data))

@app.route('/update/vendor',methods=['POST'])
def update_vendor():
  Vendor.update(request.form)
  return redirect('/vendors')
  # if Building.validate_building(request.form):
  #       Building.update(request.form)
  #       return redirect('/buildings')
  # return redirect(request.referrer)