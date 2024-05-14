import json

def read_json():
    with open('./ui_with_react/public/update.json', 'r') as file:
        data = json.load(file)
    return data

def write_json(data):
    with open('./ui_with_react/public/update.json', 'w') as file:
        json.dump(data, file, indent=4)

        
