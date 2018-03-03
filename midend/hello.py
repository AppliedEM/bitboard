from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route("/hello/")
def hello_world():
	return "Hello, world!"

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
