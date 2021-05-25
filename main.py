from dbase import Database
from classes import Json  
from flask import Flask, render_template, redirect


# instanciate db
db = Database('phonebook')

records = Json()
db.insert_data(records.get_data())

app = Flask(__name__)

@app.route('/')
def home():
  data = db.read()
  return render_template('home.html', data=data)


@app.route('/contact/<slug>')
def phone(slug):
  row_id = db.get_id('slug', slug)
  data = db.read_by_id(row_id)
  title = data['firstname'] + " " + data['lastname']
  return render_template('phone.html', title=title, data=data)

app.run(host='0.0.0.0', port=8080)
