from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[^0-9]+$')
PASSWORD_REGEX = re.compile(r'^.*[0-9]+.*[A-Z]+.*|.*[A-Z]+.*[0-9]+.*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
    valid_first_name = valid_last_name = valid_email = valid_password = False
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name cannot contain numbers.")
    else:
        valid_first_name = True
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name cannot contain numbers.")
    else:
        valid_last_name = True
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email address is invalid!")
    else:
        valid_email = True
    if request.form['password'] != request.form['confirm_password']:
        flash("Password confirmation does not match.")
    elif len(request.form['password']) < 9:
        flash("Password must be more than 8 characters!")
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Password must contain at least one capital letter and at least one number")
    else:
        valid_password = True
    if valid_first_name and valid_last_name and valid_email and valid_password:
        flash('Thanks for submitting your information.')
    return redirect('/')
app.run(debug=True)
