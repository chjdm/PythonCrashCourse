favorite_languages = {
    'liuwei': 'python',
    'peter': 'c',
    'sarah': 'ruby',
    'phil': 'python',
    'jen': 'c#'
    }

# for name, language in sorted(favorite_languages.items()):
#     print('\nname:' + name)
#     print('language: ' + language)

# friends = ['peter', 'shelly', 'phil', 'liuwei']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("Hi " + name.title() +
#               ", I see you favorite language is " +
#               favorite_languages[name].title() + ".")

print("The following languages have been mentioned:")
for value in set(favorite_languages.values()):
    print(value.title())