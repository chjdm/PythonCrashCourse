class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_format_name(self):
        format_name = self.make + "  " + self.model + "  "  + str(self.year)
        return format_name.title()

    def update_odometer(self, miles):
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print("You can't roll odometer back.")

    def read_odometer(self):
        print("This car has a odometer of " + str(self.odometer) + " miles.")
        # return self.odometer

    def increase_odometer(self, miles):
        self.odometer += miles


my_audi = Car('audi', 'A6', 2016)

print(my_audi.get_format_name())

my_audi.update_odometer(34)
my_audi.read_odometer()

my_audi.increase_odometer(3500)
my_audi.read_odometer()