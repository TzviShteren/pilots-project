import json
from model.TargetsModel import TargetModel

def read_from_json(filename: str) -> list:
    with open(filename, 'r') as jsonfile:
        return json.load(jsonfile)

def read_targets_from_json(filename: str) -> list[TargetModel]:
    return [TargetModel(item[0], item[1]) for item in read_from_json(filename)]
