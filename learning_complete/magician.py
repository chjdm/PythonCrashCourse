def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    while magicians:
        current_magician ="The great " + magicians.pop()
        new_magicians.append(current_magician)


new_magicians = []
magicians = ['jade', 'pici', 'lindee']
make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
