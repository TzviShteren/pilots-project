import csv
from model import operation


def write_operations_to_csv(operations: list[operation], filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile,
                                        fieldnames=['target city', 'priority', 'assigned pilot', 'assigned aircraft',
                                                    'distance',
                                                    'weather conditions',
                                                    'pilot skill', 'aircraft speed', 'fuel capacity',
                                                    'mission fit score'])

            csv_writer.writeheader()

            for operation in operations:
                csv_writer.writerow({
                    'target city': operation.target_city,
                    'priority': operation.priority,
                    'assigned pilot': operation.assigned_pilot,
                    'assigned aircraft': operation.assigned_aircraft,
                    'distance': operation.distance,
                    'weather conditions': operation.weather_conditions,
                    'pilot skill': operation.pilot_skill,
                    'aircraft speed': operation.aircraft_speed,
                    'fuel capacity': operation.fuel_capacity,
                    'mission fit score': operation.mission_fit_score
                })
    except Exception as e:
        print(e)
