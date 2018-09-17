def count_words(filename):

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file {} don't exist.".format(filename)
        print(msg)
    else:
        word = contents.split()
        num_word = len(word)
        print("The file {0} has about {1} words.".format(filename, num_word))


filenames = ['alice.txt', 'see.txt', 'pi.txt']
for filename in filenames:
    count_words(filename)
