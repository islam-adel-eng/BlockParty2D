import json
import os

default_data = {"Games": 0, "Rounds": 0, "Highest": 0}

def path(file):
     return file

def write(data):
    with open(path("Resources/data.txt"), "w") as data_file:
        json.dump(data, data_file)

def read():
        try:
            with open(path("Resources/data.txt")) as data_file:
                data = json.load(data_file)
            return data
        except:
             with open(path("Resources/data.txt"), "w") as data_file:
                  json.dump(default_data, data_file)
             return default_data

