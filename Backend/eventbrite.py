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
              "expand": "organizer,venue"
              }
)
data = response.json()

new_data = []

for event in data["events"]:
    new_data += [ {\
                   "name": event["name"]["text"], \
                   "organizer": event["organizer"]["name"], \
                   "description": event["description"]["html"], \
                   "latitude": event["venue"]["latitude"], \
                   "longitude": event["venue"]["longitude"], \
                   "localized_address_display": event["venue"]["address"]["localized_address_display"], \
                   } ]

print(json.dumps(new_data, sort_keys=True, indent=4))
