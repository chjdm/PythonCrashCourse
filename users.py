class User():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.user_info = ''

    def describe_user(self):
        print(self.first.title() + " " + self.last.title() + " is a " +
              self.user_info + ".")

    def greet_user(self, greet_words):
        print("Hello, " + self.first.title() + " " + self.last.title() + ", "
                                                                    "" + greet_words)

gimmi = User('Gimmi', 'gilson')
gimmi.describe_user()
gimmi.greet_user('enjoy your self.')