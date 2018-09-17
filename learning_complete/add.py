print("Give me two number, i give you answer.")
print("Anytime, enter a 'q' to exit.")

while True:
    num1 = input("Enter first number:")
    if num1 == 'q':
        break
    num2 = input("Enter second number:")
    if num2 == 'q':
        break

    try:
        res = int(num1) + int(num2)
    except ValueError:
        print("A letter can't be added.")
    else:
        print("{0} + {1} = {2}".format(num1, num2, res))

