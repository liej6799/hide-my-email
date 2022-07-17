import json

def read_file(path):
    with open(path, 'r') as file:
        obj = json.loads(file.read())
        return obj
