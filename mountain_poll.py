reponses = {}

polling_active = True

while polling_active:
    name = input("your name")
    mountain = input("your mountain")

    reponses[name] = mountain

    repeat = input(print("Would you like to do another poll?(yes/no)"))
    if repeat == 'no':
        polling_active = False

print(reponses)