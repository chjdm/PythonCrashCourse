users = {
    'liuwei': {
        'first': 'liu',
        'last': 'wei',
        'location': 'wuhan'
    },
    'aeistain': {
        'first': 'albert',
        'last': 'eistain',
        'location': 'LA'
    }
}
for username, userinfor in users.items():
    print("Username: " + username.title())
    fullname = userinfor['first'] + " " +userinfor['last']
    location = userinfor['location']
    print("\tName: " + fullname.title() + "\tLacation: " + location.title())

print(users.items())