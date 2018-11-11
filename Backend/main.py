import locations, bluebikes, eventbrite
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# form is gonna send this dude to /wow
@app.route("/wow", methods=[ "GET", "POST" ])
def main():
    # print(request.form)
    address = request.form["serial"]
    step1 = latlongAddress(address)
    step2 = getNearestStation(step1[0], step1[1])
    lat, long = step2['lat'], step2['lon']
    step3 = getEvents(lat, long)
    return render_template("index.html")

@app.route("/")
def homepage():
    return render_template("index.html")
