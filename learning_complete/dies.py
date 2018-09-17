from random import randint

class Dies():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dies(self):
        num = randint(1, self.sides)
        print("The dies of {0} sides roll to {1}.".format(self.sides, num))

dies_of_6_sides = Dies()
for num in range(0, 6):
    dies_of_6_sides.roll_dies()

print('-'*30)

dies_of_10_sides = Dies(10)
for num in range(0, 10):
    dies_of_10_sides.roll_dies()

print('-'*30)

dies_of_10_sides = Dies(20)
for num in range(0, 10):
    dies_of_10_sides.roll_dies()

