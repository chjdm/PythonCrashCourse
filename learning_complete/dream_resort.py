dream_resorts = {}

active = True

while active:
    name = input("Thank you for take in the poll, what's your name, please?")
    resort = input("If you could visit one place in the world, where would you go?")
    dream_resorts[name] = resort

    repeat = input("Would you like to take another poll?(yes/no)")

    if repeat == "no":
        active = False

for name, resort in dream_resorts.items():
    print(name.title() + " like go to " + resort.title() + ".")