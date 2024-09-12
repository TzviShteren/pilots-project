import csv
from typing import List
#from model.person import Person
from toolz import  pipe, partial

def read_people_from_csv(filepath: str) -> List[Person]:
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            return pipe(
                [row for row in reader],
                partial(map, lambda p: Person(p["name"], p["age"])),
                list
            )
    except Exception as e:
        print(e)
        return []



def write_person_to_csv(person: Person, filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['name', 'age'])
            csv_writer.writeheader()

            csv_writer.writerow({
                'name': person.name,
                'age': person.age
            })
    except Exception as e:
        print(e)

def write_people_to_csv(people: List[Person], filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['name', 'age'])
            csv_writer.writeheader()

            for person in people:
                csv_writer.writerow({
                    'name': person.name,
                    'age': person.age
                })
    except Exception as e:
        print(e)