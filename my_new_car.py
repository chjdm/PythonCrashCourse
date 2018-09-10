from car import Car, ElectricCar


my_tesla = ElectricCar('Tesla', 'Model-s', '2017')
my_tesla.get_format_name()

my_tesla.battery.get_rang()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_rang()