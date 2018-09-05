prompt = "Enter a topping, and we'll add it in,"
prompt += "\nEnter quit to exit.>"

active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print("\tOk, we'll add %s on the pizza." % topping.upper())
