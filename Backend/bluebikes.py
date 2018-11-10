import requests
import math
import sys

start_station = None
end_station = None

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

def main():
#   uri = 'https://gbfs.bluebikes.com/gbfs/gbfs.json'
  url = 'https://gbfs.bluebikes.com/gbfs/en/station_information.json'
  response = requests.get(url)
  ret = response.json()
  # for x in ret['data']['en']['feeds']:
  #   print(x) 
  count = 0
  simple = ret['data']['stations']
  for x in simple:
    # print(x)
    lon = x['lon']
    lat = x['lat']
    pair = '(' + str(lat) + ', ' + str(lon) + ')'
    lon_lat_dic[pair] = x
    # if count == 3:
    #   break
    # count += 1
  x = closestStation(42, 32) 
  print(x)
main()