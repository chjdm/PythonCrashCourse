print("Give me two numbers, and I'll divide it.")
print("Enter a 'q' to exit")

while True:


    first_number = input("Enter first number:")
    if first_number == 'q':
        break

    second_number = input("Enter second number:")
    if second_number == 'q':
        break
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("A letter can't be divide.")
    else:
        print("{0} / {1} = {2}".format(first_number, second_number, result))
