file_name = 'learning_python.txt'

with open(file_name) as learning_python:
    contences = learning_python.read()

contences.replace('python', 'c')
print(contences)

message = "I really like dogs."

print(message.replace('dog', 'cat'))

with open(file_name) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.replace('python', 'C++').rstrip())