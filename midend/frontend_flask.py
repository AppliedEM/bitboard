from flask import Flask
from flask import request
app = Flask(__name__)
import transact

use_testnet = True
@app.route('/')
def index():
	print(request.args)
	return app.send_static_file('index.html')

@app.route("/hello/")
def hello_world():
	return "Hello, world!"

@app.route('/mymoney')
def get_balance():
	global use_testnet
	utxos = transact.grab_utxos(str(request.args['account_id']),use_testnet)
	balance = transact.sum_utxos(utxos)
	return str(balance)

@app.route('/sendmoney')
def send_money():
	global use_testnet
	#print(request.args)
	account_id = str(request.args['account_id'])
	target = str(request.args['target_addr'])
	price = int(request.args['price'])
	
	new_transdata = transact.new_transaction(account_id,target,price,use_testnet)
	#print(new_transdata)
	push_attempt = transact.push_transaction(new_transdata,use_testnet) #update heree
	return str(push_attempt)
	
@app.route("/testpost/",methods=["GET","POST"])
def test_post():
	if request.method=="GET":
		return "Hello, world!"
	else:
		print("Request data")
		print(request.data)
		print("Request values")
		print(request.values)
		print("Request form stuff")
		print(request.form)
		print(request.cookies)
		#print(
		return "hi"

@app.route('/<path:path>')
def get_static(path):
	return app.send_static_file(path)
