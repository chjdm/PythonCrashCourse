pet_0 = {
    'type': 'dog',
    'name': 'petty',
    'owener': 'keying'
}

pet_1 ={
    'type': 'cat',
    'name': 'shelly',
    'owener': 'liuyuxuan'
}

pet_2 ={
    'type': 'dog',
    'name': 'wangwang',
    'owener': 'liuyuxuan'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet['name'].title() + "is a " + pet['type'] + ", he is owend by " + pet['owener'].title() + "!"  )