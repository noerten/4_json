import json
import pprint
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data


def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    file_name = input('Enter file name/path: ')
    data = load_data(file_name)
    pretty_print_json(data)
