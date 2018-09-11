try:
    file_name = 'dogs.txt'
    with open(file_name) as dog_file:
        dogs_name = dog_file.read()
except FileNotFoundError:
    pass
else:
    print(dogs_name)

try:
    file_name = 'cats.txt'
    with open(file_name) as cat_file:
        cats_name = cat_file.read()
except FileNotFoundError:
    pass
else:
    print(cats_name)
