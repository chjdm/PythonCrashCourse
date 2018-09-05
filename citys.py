citys = {
    'wuhan': {
        'country': 'china',
        'population': 8000000,
        'fact': 'the biggist city in the middle of china'
    },
    'tokyo': {
        'country': 'japan',
        'population': 28000000,
        'fact': 'the capital city of japan'
    },
    'new york': {
        'country': 'USA',
        'population': 20000000,
        'fact': 'the richest city in the world'
    }
}

for city_name, city_detail in citys.items():
    print(city_name.title() + " is a city of " + city_detail['country'].upper()
          + ", has " + str(city_detail['population'])
                           + " people, and is " + city_detail['fact'] + ".")