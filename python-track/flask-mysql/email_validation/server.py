from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

mysql = MySQLConnector(app, 'user_email_db')
# print mysql.query_db("select * from users")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    valid_email = False
    prev_emails = [user['email'] for user in mysql.query_db("select email from users")]
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email address is invalid!")
    elif request.form['email'] in prev_emails:
        flash("This email address has already been used!")
    else:
        valid_email = True
    if valid_email:
        dbkeys = "`email`, created_at"
        dbvals = ":email, NOW()"
        mysql.query_db("insert into users ({}) values ({})".format(dbkeys, dbvals), request.form)

        flash('The email address you submitted, {}, is valid!'.format(request.form['email']))
        return redirect('/results')
    else:
        return redirect('/')


@app.route('/results')
def results():
    previous = mysql.query_db("select * from users", session)
    return render_template('results.html', previous=previous)

@app.route('/delete', methods=["POST"])
def delete_email():
    mysql.query_db("delete from users where users.id = :id", request.form)
    return redirect('/results')

app.run(debug=True)
