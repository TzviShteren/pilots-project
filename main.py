import json
import requests
from utils import calculations as calcu
from model import operation

My_Api_key = "bf47316e4a70a4097f5c6d36e53530e3"


if __name__ == '__main__':
    pass




# Getting the coordinates of each country and entering into a json file
# The function will only run once so there won't be too many requests to the API
def getting_coordinates():
    with open("json_files/targets.json", 'r') as jsonfile:
        list_of_targets = json.load(jsonfile)
    list_of_city = list(map(lambda x: x["City"], list_of_targets))
    list_of_city.append("Jerusalem")
    city_coordinates = {}
    for city in list_of_city:
        API_URL = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={My_Api_key}'
        result = requests.get(API_URL).json()
        if result:  # Ensure we received valid data
            lat = result[0]["lat"]
            lon = result[0]["lon"]
            city_coordinates[city] = [lat, lon]
    with open("json_files/city_coordinates.json", 'w') as jsonfile:
        json.dump(city_coordinates, jsonfile, indent=4)  # I learned it on my own
