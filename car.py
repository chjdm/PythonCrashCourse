class Car():
    '''制造商，型号，出厂年份'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas_tank = 50

    def get_format_name(self):
        format_name = self.make + "  " + self.model + "  "  + str(self.year)
        print(format_name)
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

    def fill_gas_tank(self):
        self.gas_tank = 100


class ElectricCar(Car):
    '''制造商，型号，出厂年份'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Bettery()

    def fill_gas_tank(self):
        print("The car hasn't a gas tank!")


class Bettery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("The car has a {}-KWH battery.".format(self.battery_size))

    def get_rang(self):
        if self.battery_size == 70:
            range = 250
        elif self.battery_size ==85:
            range = 300
        message = "This car can go approximately {} miles on a full " \
                  "charge.".format(range)
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("The battery of this car has up to 85-KWH.")
