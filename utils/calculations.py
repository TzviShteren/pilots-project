import math


# Function to calculate the distance between two coordinates using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0  # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
                                                                                     2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance


def weather_score(weather):
    if weather["condition"] == "Clear":
        return 1.0
    elif weather["condition"] == "Clouds":
        return 0.7
    elif weather["condition"] == "Rain":
        return 0.4
    elif weather["condition"] == "Stormy":
        return 0.2
    else:
        return 0


def difficulty_level_task(weather: str, clouds, wind):
    return (weather_score(weather) + clouds // 10 + wind) * 100


weights = {
    "distance": 0.20,
    "priority": 0.25,
    "pilot_skill": 0.25,
    "weather_conditions": 0.20,
    "execution_time": 0.10
}

"""
"priority": 0.25,
weights = {
    "Pilot weather expertise": 0.25,
    "priority": 0.30,
    "distance": 0.20,
    "0": 0.25,  # ---------------------------------------
}
"""
