import requests, json
with open("./api_key.txt", "r") as token_file:
    MYTOKEN = token_file.read()[:-1]

address = "Boston"
within = "1km"
latitude = ""
longitude = ""
sort_by = ""

response = requests.get(
    "https://www.eventbriteapi.com/v3/events/search/",
    headers = {
        "Authorization": "Bearer " + MYTOKEN,
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

