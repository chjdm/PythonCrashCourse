def fomatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        return first_name.title() + middle_name.title() + last_name.title()
    else:
        return first_name.title() + middle_name.title() + last_name.title()


full_name = fomatted_name('georage', 'delfy', 'bush')
print(full_name)

full_name = fomatted_name('liu', 'wei')
print(full_name)