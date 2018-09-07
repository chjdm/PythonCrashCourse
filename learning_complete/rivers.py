rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'amazon': 'brazil'
}

for river, country in rivers.items():
    print("The " + river.title() + " run throught " + country.title() + ".")

for river in rivers.keys():
    print(river)
print('*'*20)
for country in rivers.values():
    print(country)