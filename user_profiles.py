def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'eistain', location="wuhan", field='physics')
print(user_profile)

my_profile = build_profile('Liu', 'Wei', location='wuhan', department = 'Housing Managment')
print(my_profile)