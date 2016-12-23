import json
import pprint
import os


def load_json_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        json_object = json.load(data_file)
    return json_object


def pretty_print_json(json_object):
    pprint.pprint(json_object)


if __name__ == '__main__':
    file_name = input('Enter file name/path: ')
    json_object = load_json_file(file_name)
    pretty_print_json(json_object)
