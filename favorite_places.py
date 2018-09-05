favorite_places = {
    'liuwei': ['qingdao', 'shenzhen', 'guangzhou'],
    'xumin': ['wuhan'],
    'liuyuxuan': ['beijing', 'xian']
}

for name, favorite_place in favorite_places.items():
    print("\n" + name.title() + "'s favorite places is:")
    for place in favorite_place:
        print("\t" + place.title())