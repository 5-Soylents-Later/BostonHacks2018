import requests
import math
import sys
import pandas as pd

# (2) - from locations find nearest bluebike station

start_station = None
end_station = None

# bikes = pd.read_csv("Hubway_Stations_as_of_July_2017.csv")
lon_lat_dic = {}
def calcDistance(lon, lat, pair):
	pair = pair[1:-1]
	pair = pair.split(',')
	distance = math.sqrt((float(pair[1]) - lon) ** 2 + (float(pair[0]) - lat) ** 2)
	return distance

def closestStation(lo, la):
	lo = float(lo)
	la = float(la)
	minimum = 10000000000000000000000000000000000000000000000
	minimum = float(minimum)
	station = 0
	for coord in lon_lat_dic:
		distance = calcDistance(lo, la, coord)
		if distance < minimum:
			minimum = distance
			station = coord
	return [station, minimum]

def getNearestStation(urlan, urlon):
	url = 'https://gbfs.bluebikes.com/gbfs/en/station_information.json'
	response = requests.get(url)
	ret = response.json()

	count = 0
	simple = ret['data']['stations']
	# print(simple)
	for x in simple:
    # print(x)
		lon = x['lon']
		lat = x['lat']

		pair = '(' + str(lat) + ', ' + str(lon) + ')'
		lon_lat_dic[pair] = x

	x = closestStation(urlan, urlon)

	return lon_lat_dic[x[0]]