import json
import os


def load_json_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:
        json_object = json.load(data_file)
    return json_object


def pretty_print_json(json_object):
    print(json.dumps(json_object, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    file_name = input('Enter file name/path: ')
    json_object = load_json_file(file_name)
    pretty_print_json(json_object)
