from flask import Flask
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request
from flask import redirect


# Create Database to store the values

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banderhata.db'   # /// is a relative path; //// is an absulute path
db = SQLAlchemy(app)   #initialize database with settings from 'app'

class Elec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r>' % self.id

class Gas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r>' % self.id

class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r>' % self.id

# Electricity Routes

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/electricity', methods=['POST', 'GET'])   # POST request will send data to our database 
def electricity():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Elec(content=task_content)

        try:   # push to the database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/electricity')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Elec.query.order_by(Elec.date_created).all()   # query the database; alternative end first(); how we display all tasks in table
        return render_template('electricity.html', tasks=tasks)

@app.route('/delete_elec/<int:id>')
def delete_elec(id):
    task_to_detele = Elec.query.get_or_404(id)

    try:
        db.session.delete(task_to_detele)
        db.session.commit()
        return redirect('/electricity')
    except:
        return 'There was a problem deleting that task'

@app.route('/update_elec/<int:id>', methods=['POST', 'GET'])
def update_elec(id):
    task = Elec.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/electricity')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update_elec.html', task=task)

# Gas Routes

@app.route('/gas', methods=['POST', 'GET'])   # POST request will send data to our database 
def gas():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Gas(content=task_content)

        try:   # push to the database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/gas')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Gas.query.order_by(Gas.date_created).all()   # query the database; alternative end first(); how we display all tasks in table
        return render_template('gas.html', tasks=tasks)

@app.route('/delete_gas/<int:id>')
def delete_gas(id):
    task_to_detele = Gas.query.get_or_404(id)

    try:
        db.session.delete(task_to_detele)
        db.session.commit()
        return redirect('/gas')
    except:
        return 'There was a problem deleting that task'

@app.route('/update_gas/<int:id>', methods=['POST', 'GET'])
def update_gas(id):
    task = Gas.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/gas')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update_gas.html', task=task)

# Water Routes

@app.route('/water', methods=['POST', 'GET'])   # POST request will send data to our database 
def water():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Water(content=task_content)

        try:   # push to the database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/water')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Water.query.order_by(Water.date_created).all()   # query the database; alternative end first(); how we display all tasks in table
        return render_template('water.html', tasks=tasks)

@app.route('/delete_water/<int:id>')
def delete_water(id):
    task_to_detele = Water.query.get_or_404(id)

    try:
        db.session.delete(task_to_detele)
        db.session.commit()
        return redirect('/water')
    except:
        return 'There was a problem deleting that task'

@app.route('/update_water/<int:id>', methods=['POST', 'GET'])
def update_water(id):
    task = Water.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/water')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update_water.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)