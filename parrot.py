prompt = "Tell me something, and I will repeat it back to you,"
prompt += "\nEnter 'quit' to exit:>"

flag = True

while flag:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

