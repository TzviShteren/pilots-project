import json
import orderby
import requests
from utils import calculations, receiving_information
from repository import json_repository, csv_repository
from model.possible_mission import PossibleMission

My_Api_key = "bf47316e4a70a4097f5c6d36e53530e3"


# f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={My_Api_key}'


# Receiving information about the weather in a certain country (returns according to the relevant time)
def Weather_in__certain_country(result):
    srt_of_day = receiving_information.show_upcoming_date()
    return next(filter(lambda x: x["dt_txt"] == srt_of_day, result["list"]), False)


# Returns a list of all cities
def get_all_city() -> list[str]:
    list_of_targets = json_repository.read_from_json("json_files/targets.json")
    list_of_city = list(map(lambda x: x["City"], list_of_targets))
    return list_of_city


# Getting the coordinates end the weather of each country and entering into a json file
# The function will only run once so there won't be too many requests to the API
def getting_coordinates():
    list_of_city = get_all_city()
    city_coordinates_end_weather = []
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
            city_coordinates_end_weather.append({"City": city, "weather": weather, "clouds": clouds, "wind": wind,
                                                  "coordinates": {"lat": lat, "lon": lon}})

    with open("json_files/city_coordinates.json", 'w') as jsonfile:
        json.dump(city_coordinates_end_weather, jsonfile, indent=4)  # I learned it on my own


if __name__ == '__main__':
    # getting_coordinates()
    # exit(1)
    list_of_targets = json_repository.read_from_json("json_files/city_coordinates.json")
    list_of_pilots = json_repository.read_from_json("json_files/pilots.json")
    list_of_targets_level = json_repository.read_from_json("json_files/targets.json")
    # list_of_targets_level.sort(key=lambda x: x["Priority"], reverse=True)
    list_of_aircrafts = json_repository.read_from_json("json_files/aircrafts.json")
    to_csv = []
    for targets_level in list_of_targets_level:
        data = next(filter(lambda x: x["City"] == targets_level["City"], list_of_targets), False)
        for pilot in list_of_pilots:
            for aircraft in list_of_aircrafts:
                pm = PossibleMission(
                    targets_level["City"],
                    targets_level["Priority"],
                    pilot["name"],
                    pilot["skill_level"],
                    aircraft["type"],
                    calculations.haversine_distance(data["coordinates"]["lat"], data["coordinates"]["lon"]
                                                    , receiving_information.coordinates_Jerusalem[0]
                                                    , receiving_information.coordinates_Jerusalem[1]),
                    calculations.difficulty_level_task(data["weather"], data["clouds"], data["wind"])
                )
                

