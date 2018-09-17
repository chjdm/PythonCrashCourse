from name_function import get_formatted_name

while True:
    print("Enter a 'q' for exit any time:")
    firtname = input("Enter your first name:")
    if firtname == 'q':
        break
    lastname = input("Enter your last name:")
    if lastname == 'q':
        break
    fullname = get_formatted_name(firtname, lastname)
    print("\tNeatly full name: " + fullname)