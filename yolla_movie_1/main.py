from flask import Flask, jsonify, request, render_template
from model import *
from database import *
		

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		uname = request.form['username']
		pword = request.form['password']

		if query_by_name(uname) != None:
			return render_template('signup.html', errormsg = "some thing is wrong, try again")			
		else:
			create_user(uname, pword)
			return render_template('signup.html', successmsg = "success")


@app.route('/signin',methods=['GET', 'POST'] )
def signin():
	if request.method == 'GET':
		return render_template('signin.html')
	else:
		uname = request.form['username']
		pword = request.form['password']

		if query_by_name(uname) == None:
			return render_template('signin.html', errormsg = " some thing is wrong, try again  ")
		else: 
			if query_by_name(uname).passward != pword:
				return render_template('signin.html', errormsg = "password wrong, try again")
			else: 
				return render_template('signin.html',us = uname, successmsg = " success ")
				
	return render_template("signin.html")




app.run(debug = True, host="localhost", port="5000")

