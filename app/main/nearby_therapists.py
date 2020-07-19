import json
import urllib.request
import requests
from pprint import pprint

API_KEY = "AIzaSyD_ZzLSJXWgCQeONsk0KCf6x3_XKQ610qE"

def nearby(zip_code):
    lat = float()
    lon = float()
    with urllib.request.urlopen('https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q={}&facet=state&facet=timezone&facet=dst'.format(zip_code)) as response:
        loc = json.loads(response.read())
        lat, lon = loc['records'][0]['fields']['geopoint']
        # print(lat, lon)

    # with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/nearbysearch/output?key={}&location={},{}&radius={}&keyword={}'.format(zip_code, lat, lon, 5000, "therapists")) as response:
    #     loc = json.loads(response.read())
    #     print(loc)

    # url = "https://maps.googleapis.com/maps/api/place/nearbysearch/output?key={}&location={},{}&radius={}&keyword={}".format(API_KEY, lat, lon, 5000, "therapists")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}&location={},{}&radius={}".format("therapists near me", API_KEY, lat, lon, "2000" )
    # print(url)

    r = requests.get(url)
    r = json.loads(r.text)
    results = []
    for result in r['results']:
        results.append((result['name'], result['formatted_address']))
    return(results)


# nearby("02459")