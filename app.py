from flask import Flask
from Backend import *

app = Flask(__name__)

@app.route("/output")
def output():
	return eventbrite.getEvents("","","40","-20","")
