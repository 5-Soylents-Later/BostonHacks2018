import requests, json
from Keys import EBrite

def getEvents(add, within, lat, long, sort_by):
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
        params = {"location.address": add, \
                  "location.within": within, \
                  "location.latitude": lat, \
                  "location.longitude": long, \
                  #sort_by: “date”, “distance” and “best”. Prefix with a hyphen to reverse the order, e.g. “-date”
                  "sort_by": sort_by, \
                  }
    )
    data = response.json()
    return data

print(json.dumps(data, sort_keys=True, indent=4))
