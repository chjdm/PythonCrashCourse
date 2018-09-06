def city_country(city, country):
    rst = city.title() + ", " + country.title()
    return rst

print(city_country('beijing', 'china'))
print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
