from Keys import GMaps
import requests
import pandas as pd



def latlongAddress(id):

    bikes = pd.read_csv("Hubway_Stations_as_of_July_2017.csv")
    lat = bikes.loc[id]['Latitude']
    long = bikes.loc[id]['Longitude']
    
    URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+ str(lat) + "," + str(long) + "&key=" + GMaps
    r = requests.get(url = URL)
    data = r.json()
    return data["results"][0]["formatted_address"]



# print(latlongAddress(42.325333, -71.075354))
