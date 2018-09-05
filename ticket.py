active = True
while active:
    age = input("Enter you age, quit for exit.>")
    if age == 'quit':
        break
    elif int(age) <= 3:
        print("It's free for you.")
        continue
    elif int(age) <= 12:
        print("The ticket price for age %d is $10." % int(age))
        continue
    elif int(age) > 12:
        print("The ticket price for age %d is $15." % int(age))