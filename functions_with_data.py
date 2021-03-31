import json


def read_json_file(file):
    with open(file, 'r') as file_handle:
        data = json.load(file_handle)
    return data


def write_to_json_file(file, data):
    with open(file, 'w') as file_handle:
        json.dump(data, file_handle)
