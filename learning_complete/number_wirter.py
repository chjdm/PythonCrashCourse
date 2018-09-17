import json

file_name = 'number.json'

numbers = [1, 2, 3, 4, 5]

with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)