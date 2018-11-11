# from .Keys import GMaps
from Keys import GMaps
import requests
import pandas as pd

# (1) - From front end to here

def latlongAddress(add):

    bikes = pd.read_csv("Hubway_Stations_as_of_July_2017.csv")
    address = add.replace(" ", "+")
    # URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+ str(lat) + "," + str(long) + "&key=" + GMaps
    URL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + GMaps
    r = requests.get(url = URL)
    data = r.json()
    print(data)
    return [data["results"][0]["geometry"]["location"]["lat"], data["results"][0]["geometry"]["location"]["lng"]]
