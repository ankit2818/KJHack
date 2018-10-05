from flask import Flask, session, redirect, url_for, escape, request
import pymysql

db = pymysql.connect("localhost","root","","Minutes_io")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()

app = Flask(__name__)
app.secret_key = "KJHack"
# @app.route('/')
# def hello_world():
# 	return "Hello"

@app.route('/')
def index():
 	if 'username' in session:
 		#username=session['username']
 		return "logged in"
 	return "please log in"


@app.route('/login', methods = ['GET','POST'])
def login():
	if(len(request.form['useremail'])==0):
	 	session['useremail'] = request.form['useremail']
	 	return redirect(url_for('index'))
	else:
		return "Do OAUTH"

@app.route('/logout')
def logout():
	session.pop('useremail',None)
	return redirect(url_for('login'))
   #calls the function index


if __name__ == '__main__':
	app.run(debug = True)