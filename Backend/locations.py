from Keys import GMaps
import requests
import pandas

def latlongAddress(lat, long):
    URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+ str(lat) + "," + str(long) + "&key=" + GMaps
    r = requests.get(url = URL)
    data = r.json()
    return data["results"][0]["formatted_address"]

# print(latlongAddress(42.325333, -71.075354))
