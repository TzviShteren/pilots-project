import json


def read_from_json(filename: str) -> list:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data
