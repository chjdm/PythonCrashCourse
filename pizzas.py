def make_pizza(size, *toppings):
    print("Makeing {0} inchs pizza with the following toppings:".format(size))
    for topping in toppings:
        print("- " + topping)


# make_pizza('16', 'pepperoni', 'mushroom', 'green peper')
# make_pizza('9', 'extra cheese')
