class Dog():
    """第一个类，小狗的简单尝试"""

    def __init__(self, name, age):
        """init name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗坐下"""
        print(self.name.title() +" is sitting now.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " roll over here.")

mydog = Dog('Lily', 13)
mydog.roll_over()
mydog.sit()

print("My dog is " + str(mydog.age) + " years old.")



