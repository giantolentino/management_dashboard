from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
  if 'user_id' not in session:
      return redirect('/logout')
  data ={
      'id': session['user_id']
  }
  user = User.get_by_id(data)
  return render_template("dashboard.html", user=user)

@app.route('/add/manager')
def add_manager():
  return render_template("add_manager.html")

@app.route('/register/manager',methods=['POST'])
def register_manager():
  data ={ 
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'],
    "password": bcrypt.generate_password_hash(request.form['password'])
    }
  id = User.save(data)
  return redirect('/add/manager')

@app.route('/managers')
def managers():
  managers = User.get_all()
  return render_template("managers.html", managers=managers)

@app.route('/destroy/manager/<int:id>')
def delete_manager(id):
  data ={
      'id': id
  }
  User.destroy_manager(data)
  return redirect('/managers')

@app.route('/manager/<int:id>')
def show_manager(id):
  data = {
      "id": id
  }
  manager = User.get_by_id(data)
  return render_template('show_manager.html', manager=manager)

@app.route('/edit/manager/<int:id>')
def edit_manager(id):
  data ={ 
      "id":id
  }
  return render_template("edit_manager.html",manager=User.get_by_id(data))

@app.route('/update/manager',methods=['POST'])
def update_manager():
  User.update(request.form)
  return redirect('/managers')