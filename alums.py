def make_alums(singer, alum_name, songs=''):
    alum_info = {'singer': singer, 'name': alum_name}
    if songs:
        alum_info['songs'] = songs
    return alum_info

while True:
    print("Now make a alum, 'q' for exit at any time:")
    singer_name = input("Enter the singer name:")
    if singer_name == 'q':
        break
    alum_name = input("Enter the alum name:")
    if alum_name == 'q':
        break

    alum = make_alums(singer_name,  alum_name)

    message = "The singer of alum " + alum['name'] +" is " + alum['singer'] + "."
    print(message)
