favorite_languages = {
    'liuwei': ['python', 'java'],
    'peter': ['c', 'list'],
    'sarah': ['ruby'],
    'phil': ['python'],
    'jen': ['c#', 'java']
    }

for name, favorite_language in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in favorite_language:
        print('\t' + language.title())


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

# print("The following languages have been mentioned:")
# for value in favorite_languages.values():
#     print(value)
#
# interviewers = ['liuwei', 'silly', 'jen', 'charli', 'susan']
#
# for interviewer in interviewers:
#     if interviewer in favorite_languages.keys():
#         print("%s,Thank you for interview!" %interviewer)
#     else:
#         print("%s, you are invited to interview!" %interviewer)