from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[^0-9]+$')
PASSWORD_REGEX = re.compile(r'^.*[0-9]+.*[A-Z]+.*|.*[A-Z]+.*[0-9]+.*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create_user():
    valid_first_name = valid_last_name = valid_email = valid_password = False
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['confirm_password']

    if len(first_name) < 3:
        flash("First name must be longer than 2 characters!", "register")
    elif not NAME_REGEX.match(first_name):
        flash("First name cannot contain numbers.", "register")
    else:
        valid_first_name = True

    if len(last_name) < 3:
        flash("Last name must be longer than 2 characters!", "register")
    elif not NAME_REGEX.match(last_name):
        flash("Last name cannot contain numbers.", "register")
    else:
        valid_last_name = True

    prev_emails = [user['email'] for user in mysql.query_db("select email from users")]
    if len(email) < 1:
        flash("Email cannot be blank!", "register")
    elif not EMAIL_REGEX.match(email):
        flash("Email address is invalid!", "register")
    elif request.form['email'] in prev_emails:
        flash("This email address has already been used!", "register")
    else:
        valid_email = True

    if password != password_confirmation:
        flash("Password confirmation does not match.", "register")
    elif len(password) < 9:
        flash("Password must be more than 8 characters!", "register")
    elif not PASSWORD_REGEX.match(password):
        flash("Password must contain at least one capital letter and at least one number", "register")
    else:
        valid_password = True
        encrypted_pass = bcrypt.generate_password_hash(password)

    if valid_first_name and valid_last_name and valid_email and valid_password:
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': encrypted_pass
        }
        dbkeys = "`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`"
        dbvals = ":first_name, :last_name, :email, :password, NOW(), NOW()"
        mysql.query_db("insert into users({}) values ({})".format(dbkeys, dbvals), data)
        flash('Thanks for submitting your information.')
        session['id'] = mysql.query_db("select id from users where email = :email", request.form)[0]['id']
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def success():
    name = mysql.query_db("select first_name from users where id = :id", session)[0]['first_name']
    return render_template('success.html', name=name)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = {'email': email}
    emails = [user['email'] for user in mysql.query_db("select email from users")]
    if request.form['email'] in emails:
        user_data = mysql.query_db("select * from users where users.email = :email", query)[0]
        if bcrypt.check_password_hash(user_data['password'], password):
            session['id'] = user_data['id']
            return redirect('/success')
        else:
            flash("Incorrect password!", 'login')
    else:
        flash("Email does not exist in the database.", 'login')
    return redirect('/')

@app.route('/logout', methods=['POST'])
def session_clear():
    session.clear()
    return redirect('/')


app.run(debug=True)
