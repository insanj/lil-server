from flask import Flask, request, Response
from server import * 
app = Flask(__name__)


@app.route("/")
def hello():
	page = open("talk.html", "r")
#	query = request.args.get('q')
#	return processRequest(quer)
	return Response(page.read(), mimetype="text/html")

@app.route("/json/")
def anotherThing():
	query = request.args.get('q')
	return Response("{ request : " + query + " }", mimetype="application/json")
