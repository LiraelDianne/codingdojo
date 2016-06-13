from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def info():
    warnings = False
    if len(request.form['name']) < 1:
        flash("Warning: name field cannot be empty!")
        warnings = True
    if len(request.form['comment']) < 1:
        flash('Warning: comment field cannot be empty!')
        warnings = True
    elif len(request.form['comment']) > 120:
        flash('Warning: comment field cannot be more than 120 characters!')
        warnings = True
    if warnings:
        return redirect('/')
    session["name"] = request.form['name']
    session["location"] = request.form['location']
    session["language"] = request.form['language']
    session["comment"] = request.form['comment']
    return redirect('/result')

@app.route("/result")
def displayinfo():
    return render_template('result.html')

app.run(debug=True)


