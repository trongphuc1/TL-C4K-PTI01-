import json
from data_io import load_json_data, write_json_data

def load_json_data():
    anime_dict_data = list()
    with open("data.json","r") as json_in:
        json_data = json.load(json_in)
    anime_dict_data.extend(json_data)
    return anime_dict_data

def write_json_data(json_data):
    with open("data.json","W") as json_out:
        json.dump(json_data, json_out)