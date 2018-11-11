import locations, bluebikes, eventbrite
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
if __name__ == '__main__':
   app.run(
       debug=True,
   )

# form is gonna send this dude to /wow
@app.route("/wow", methods=[ "GET", "POST" ])
def main():
    print(request.form)
    address = request.form["serial"]
    step1 = locations.latlongAddress(address)
    lat, lon = step1[0], step2[1]
    step2 = bluebikes.getNearestStation(lat, lon)
    lat, lon = step2['lat'], step2['lon']
    step3 = eventbrite.getEvents(lat, lon)
    return render_template("index.html")

@app.route("/")
def homepage():
    return render_template("index.html")
