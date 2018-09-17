file_name = 'pi_million_digits.txt'

with open(file_name) as pi_object:
    print(type(pi_object))
    lines = pi_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
#
# birthday = input("Enter your birthday, in the form yymmdd:")
# if birthday in pi_string:
#     print("Your birthday in the first million digits of PI!")
# else:
#     print("Your birthday isn't in the first million digits of PI!")

print(pi_string[:130])
print(len(pi_string))