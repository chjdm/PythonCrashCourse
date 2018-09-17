import json

file_name = 'number.json'

with open(file_name) as f_obj:
    number = json.load(f_obj)
    print(number)