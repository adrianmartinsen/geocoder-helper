import requests

# API Key - add your API key in a text-file called "api-key.txt" in project directory
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close

# base url
url = "https://maps.googleapis.com/maps/api/geocode/json?&address="

def  find_location(place):
    res = requests.get(url + place + "&key=" + api_key)
    if res.status_code == 200:
        data = res.json()
        location = data['results'][0]['geometry']['location']
        return location # location is returned as dictionary {lat: 123, lng: 456}
    else:
        print('Failed to retrieve data')
