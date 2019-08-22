import requests
import json
import geopy
import pprint
url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
# this will give us the location details of our ip
accesskey = '' # type in your access key
my_current_coordinates_url_handler = requests.get(f'http://api.ipstack.com/check?access_key={accesskey}&fields=main')
json_coordinates = json.loads(my_current_coordinates_url_handler.text)
our_lat = json_coordinates['latitude']
our_long = json_coordinates['longitude']
# We have to convert this into the
print(our_lat,' '*11,our_long)
coords_1 = our_lat,our_long


response = requests.get(url)

if response.status_code == 200:
    print("Request Successfully done")
    list_data = json.loads(response.text)
    for data in list_data:
        destination_lat = data['geolocation']['latitude']
        destination_long = data['geolocation']['longitude']
        coords_2 = destination_lat,destination_long
        print(geopy.distance.vincenty(coords_1, coords_2).km)
