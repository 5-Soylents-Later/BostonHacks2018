import requests, json
from Keys import EBrite

address = "Boston"
within = "100km"
latitude = "42"
longitude = "-70"
sort_by = ""

response = requests.get(
    "https://www.eventbriteapi.com/v3/events/search/",
    headers = {
        "Authorization": "Bearer " + EBrite,
    },
    verify = True,  # Verify SSL certificate
    params = {"location.address": address, \
              "location.within": within, \
              "location.latitude": latitude, \
              "location.longitude": longitude, \
              #sort_by: “date”, “distance” and “best”. Prefix with a hyphen to reverse the order, e.g. “-date”
              "sort_by": sort_by, \
              }
)
data = response.json()

print(json.dumps(data, sort_keys=True, indent=4))

