from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# optional second parameter methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index():
    return render_template('index.html', greeting="Hello ninjas!")

@app.route("/ninjas")
def ninjas():
    return render_template('ninjas.html')


@app.route("/dojos/new")
def dojos():
    return render_template('dojos.html')

app.run(debug=True)


