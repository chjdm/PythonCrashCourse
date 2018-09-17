class Restaurant():
    def __init__(self, restraurant_name, cuisine):
        self.restraurant_name = restraurant_name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print("We are a " + self.restraurant_name + " restaurant, and we " \
                                                  "provide " + self.cuisine \
                          + " food.")

    def open_restaurant(self):
        print("We are opening now!")

    def set_number_served(self, num):
        self.number_served = num

    def increase_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, restraurant_name, cuisine, flavor):
        super().__init__(restraurant_name, cuisine)
        self.flavor = flavor



allby = IceCreamStand('allby', '', 'italy')
print(allby.flavor)