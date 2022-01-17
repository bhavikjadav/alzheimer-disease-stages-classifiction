from email import header
from flask import Flask, render_template, redirect, request, session, flash
import sqlite3
import pandas as pd

conn = sqlite3.connect('./database/admin_auth.db')
admin_auth_data = pd.read_sql_query('SELECT * FROM admin_auth;', conn)

print(admin_auth_data)

app = Flask(__name__)
app.secret_key = 'MachineLearningisLife#123'

# Route for handling the login page logic
@app.route('/', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == admin_auth_data.iat[0, 0] and password == admin_auth_data.iat[0, 1]: 
            session['user'] = username
            return redirect('/dashboard')
        flash("Wrong Username or Password")
        return redirect('/')
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == admin_auth_data.iat[0, 0]):
        return render_template('dashboard.html')
    #here we are checking whether the user is logged in or not
    return redirect('/')  #if the user is not in the session

if __name__ == '__main__':
    app.run(debug=True)