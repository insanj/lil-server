from flask import Flask, request, Response, render_template
from server import * 
import json

app = Flask(__name__)

global_integer = 0

@app.route("/")
def hello():
	return render_template("talk.html")

@app.route("/json/")
def anotherThing():
	query = request.args.get('q')
	
	global global_integer
	global_integer = global_integer + 1
	
	responseDict = { "query" : query, "count" : global_integer }
	responseJSON = json.dumps(responseDict)
	return Response(responseJSON, mimetype="application/json")
