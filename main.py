import json
import requests
from utils import calculations, receiving_information
from repository import json_repository

from model import operation

My_Api_key = "bf47316e4a70a4097f5c6d36e53530e3"


# f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={My_Api_key}'

# Receiving information about the weather in a certain country (returns according to the relevant time)
def Weather_in__certain_country(result):
    srt_of_day = receiving_information.show_upcoming_date()
    return next(filter(lambda x: x["dt_txt"] == srt_of_day, result["list"]), False)


# Returns a list of all cities (including Jerusalem)
def get_all_city() -> list[str]:
    list_of_targets = json_repository.read_from_json("json_files/targets.json")
    list_of_city = list(map(lambda x: x["City"], list_of_targets))
    list_of_city.append("Jerusalem")
    return list_of_city


# Getting the coordinates end the weather of each country and entering into a json file
# The function will only run once so there won't be too many requests to the API
def getting_coordinates():
    list_of_city = get_all_city()
    city_coordinates_end_weather = {}
    for city in list_of_city:
        API_URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={My_Api_key}'
        result = requests.get(API_URL).json()
        if result:  # Ensure we received valid data
            lat = result["city"]["coord"]["lat"]
            lon = result["city"]["coord"]["lon"]
            filtered_for_day = Weather_in__certain_country(result)
            weather = filtered_for_day["weather"][0]["main"]
            clouds = filtered_for_day["clouds"]["all"]
            wind = filtered_for_day["wind"]["speed"]
            city_coordinates_end_weather[city] = {"weather": weather, "clouds": clouds, "wind": wind,
                                                  "coordinates": {"lat": lat, "lon": lon}}
    with open("json_files/city_coordinates.json", 'w') as jsonfile:
        json.dump(city_coordinates_end_weather, jsonfile, indent=4)  # I learned it on my own


if __name__ == '__main__':
    pass
