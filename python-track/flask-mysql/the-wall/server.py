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
mysql = MySQLConnector(app, 'the_wall')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create_user():
    valid_first_name = valid_last_name = valid_email = valid_password = False
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        }
    password = request.form['password']
    password_confirmation = request.form['confirm_password']

    if len(data['first_name']) < 3:
        flash("First name must be longer than 2 characters!", "register")
    elif not NAME_REGEX.match(data['first_name']):
        flash("First name cannot contain numbers.", "register")
    else:
        valid_first_name = True

    if len(data['last_name']) < 3:
        flash("Last name must be longer than 2 characters!", "register")
    elif not NAME_REGEX.match(data['last_name']):
        flash("Last name cannot contain numbers.", "register")
    else:
        valid_last_name = True

    prev_emails = [user['email'] for user in mysql.query_db("select email from users")]
    if len(data['email']) < 1:
        flash("Email cannot be blank!", "register")
    elif not EMAIL_REGEX.match(data['email']):
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
        data['password'] = bcrypt.generate_password_hash(password)

    if valid_first_name and valid_last_name and valid_email and valid_password:
        dbkeys = "`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`"
        dbvals = ":first_name, :last_name, :email, :password, NOW(), NOW()"
        mysql.query_db("insert into users({}) values ({})".format(dbkeys, dbvals), data)
        flash('Thanks for submitting your information.')
        session['id'] = mysql.query_db("select id from users where email = :email", request.form)[0]['id']
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    query = {'email': request.form['email']}
    emails = [user['email'] for user in mysql.query_db("select email from users")]
    if request.form['email'] in emails:
        user_data = mysql.query_db("select * from users where users.email = :email", query)[0]
        if bcrypt.check_password_hash(user_data['password'], password):
            session['id'] = user_data['id']
            return redirect('/wall')
        else:
            flash("Incorrect password!", 'login')
    else:
        flash("Email does not exist in the database.", 'login')
    return redirect('/')

@app.route('/wall')
def display_wall():
    name = mysql.query_db("select first_name from users where id = :id", session)[0]['first_name']
    user_posts = mysql.query_db("select messages.id, messages.message as content, first_name, last_name, date_format(messages.created_at, '%M %D %Y at %l:%i %p') as date, messages.user_id from messages join users on messages.user_id = users.id order by messages.created_at desc")
    comments = mysql.query_db("select comments.comment as content, first_name, last_name, date_format(comments.created_at, '%M %D %Y at %l:%i %p') AS date, comments.message_id as post_id, comments.user_id, comments.id from comments join users on comments.user_id = users.id")
    data = {
        'user_id': session['id'],
        'user_name': name
    }
    if len(user_posts) > 0:
        data['user_posts'] = user_posts
        if len(comments) > 0:
            data['comments'] = comments
    return render_template('/wall.html', data=data)

@app.route('/message', methods=['POST'])
def post_message():
    #get request.form content and put it in the database
    query_data = {
        'user_id': session['id'],
        'content': request.form['content']
    }
    query = "insert into messages (`user_id`, `message`, `created_at`, `updated_at`) values (:user_id, :content, NOW(), NOW())"
    mysql.query_db(query, query_data)
    return redirect('/wall')

@app.route('/delete_message', methods=['POST'])
def remove_message():
    query_data = {
        'id': request.form['id']
    }
    mysql.query_db('delete from messages where messages.id = :id', query_data)
    return redirect('/wall')

@app.route('/delete_comment', methods=['POST'])
def remove_comment():
    query_data = {
        'id': request.form['id']
    }
    mysql.query_db('delete from comments where comments.id = :id', query_data)
    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def post_comment():
    #get comment content and put in database
    query_data = {
        'user_id': session['id'],
        'message_id': request.form['message_id'],
        'content': request.form['content']
    }
    query = "insert into comments (`user_id`, `comment`, `created_at`, `updated_at`, `message_id`) values (:user_id, :content, NOW(), NOW(), :message_id)"

    mysql.query_db(query, query_data)
    return redirect('/wall')

@app.route('/logout', methods=['POST'])
def session_clear():
    session.clear()
    return redirect('/')


app.run(debug=True)
