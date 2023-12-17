import json
from flask import Flask, render_template, url_for,request,redirect

app = Flask(__name__, static_url_path='/static', static_folder='../static')
users_file = 'users.json'

try:
    with open(users_file, 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    users = []

name = 'Qlean'
mail = 'guyguz1@gmail.com'
students =[{"name":"Nadav","email":"nadav98@gmail.com"},{"name":"Shon","email":"shon@gmail.com"},{"name":"Guy","email":"guyguz1@gmail.com"}]


@app.route("/")
def index():

    image_url = url_for('static', filename='pictures/tekken-8.jpg')
    return render_template('index.html', image_url=image_url)

@app.route("/aboutme")
def about():

    image_url = url_for('static', filename='pictures/tekken-8.jpg')
    return render_template('about.html', image_url=image_url,data=mail)

@app.route("/students")
def create_students():
    return render_template('students.html', students = students)

@app.route("/signup" ,methods=['GET','POST'])
def signup():
    global users
    username = None
    password = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        print(users[0])
        for user in users:
            if user['username'] == username and not user['password'] == password:
                return render_template('signup.html', errormsg = 'Mail is already registered')
        users.append({'username':username,'password':password})
        return render_template('success.html')
    return render_template('signup.html')


@app.route("/login" ,methods=['GET','POST'])
def login():
    global users
    username = None
    password = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                image_url = url_for('static', filename='pictures/tekken-8.jpg')
                return render_template('index.html',user_name = user['name'],image_url=image_url)
            elif user['username'] == username and not user['password'] == password:
                return render_template('login.html', errormsg = 'password is not correct')
        else:
            return render_template('login.html', errormsg = 'User is not registered')
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)