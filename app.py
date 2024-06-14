#!/usr/bin/env python3
from flask import Flask, render_template, request
import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', database='users_db') # connect to localhost
#db = pymysql.connect(host='flask-db', user='root', password='password', database='users_db', port=3306) # Connect to conta.

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name,email) VALUES (%s,%s)", (username,email))
        db.commit()
        cursor.close()
        return "records successfully submited"
    
    return render_template('index.html')


"""
@app.route('/users')
def users():
    cursor = db.cursor()
    users = cursor.execute("SELECT * FROM users")
    if users > 0:
        userDetails = cursor.fetchall()
        return render_template('users.html', userDetails=userDetails)
"""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
