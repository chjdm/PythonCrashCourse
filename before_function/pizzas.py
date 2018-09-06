pizza = {
    'crust': 'thick',
    'topping': ['mushroom', 'extra cheese']
}

print("You order a " + pizza['crust'] + "-crust pizza, with the following topping:")
for topping in pizza['topping']:
    print("\t" + topping)
