import requests
import json
import geopy.distance
from collections import defaultdict
import pprint
url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
# this will give us the location details of our ip
accesskey = '' # type in your access key
my_current_coordinates_url_handler = requests.get(f'http://api.ipstack.com/check?access_key={accesskey}&fields=main')
json_coordinates = json.loads(my_current_coordinates_url_handler.text)
our_lat = json_coordinates['latitude']
our_long = json_coordinates['longitude']
# our_lat = -33.9122314453125
# our_long = 151.19967651367188
# We have to convert this into the
print(our_lat,' '*11,our_long)
coords_1 = our_lat,our_long


response = requests.get(url)
location_dist = defaultdict(str)
distance_list = []

if response.status_code == 200:
    print("Request Successfully done")
    list_data = json.loads(response.text)
    for data in list_data:
        try:
            destination_lat = data['geolocation']['latitude']
            destination_long = data['geolocation']['longitude']
            coords_2 = destination_lat,destination_long
            distance = geopy.distance.geodesic(coords_1, coords_2).km
            # print(distance)
            location_dist[distance] = data['name']
            distance_list.append(distance)

        except Exception as e:
            print(f"Error : {e} : {data}")

else:
    print("Something wrong with the request, please check it.")
# sorted list
distance_list.sort()
for loc in distance_list[:11]:
    # as we need top 10 location itself
    print(location_dist[loc])
