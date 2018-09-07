def build_person(first_name, last_name, age=''):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('liu', 'wei')
print(musician)
