from crypt import methods
from flask import Flask, render_template, render_template_string, url_for, redirect, session, request
from mybase64 import *
from filter import check_filter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CENSORED'

HOST = '0.0.0.0'
PORT = '1337'

@app.route('/')
def index():
	if 'user' in session:
		return redirect(url_for('dashboard'))
	return redirect(url_for('login'))

@app.route('/dashboard',methods=['GET'])
def dashboard():
	if 'user' not in session:
			return redirect(url_for('login'))
	else:
		if request.args.get('payload') is not None:
			payload = request.args.get('payload')
			if check_filter(payload):
				render_template_string(payload)
			return 'I believe you can overcome this difficulty ><'
		return 'miss params'

@app.route('/login', methods=['GET','POST'])
def login():
	if 'user' in session:
		return redirect(url_for('dashboard'))
	else:
		if request.method == "POST":
			user, passwd = '', ''
			user = request.form['user']
			passwd = request.form['passwd']
			if user == 'admin' and bdecode(passwd) == 'pass is admin ??' and len(passwd) == 24 and passwd != 'cGFzcyBpcyBhZG1pbiA/Pw==':
				session['user'] = user
				return redirect(url_for('dashboard'))
			return render_template('login.html', msg='Incorrect !')
		return render_template('login.html')

if __name__ == '__main__':
	app.run(HOST,PORT)