import locations, bluebikes, eventbrite


def main(address):
    step1 = latlongAddress(address)
    step2 = getNearestStation(step1[0], step1[1])
    step3 = getEvents(step2['lat'], step2['lon'])

    
