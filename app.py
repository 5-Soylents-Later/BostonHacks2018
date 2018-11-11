from flask import Flask
from Backend import Keys
from Backend import eventbrite, bluebikes, locations

app = Flask(__name__)

@app.route("/output")
def output():
	return eventbrite.getEvents("","","40","-20","")
