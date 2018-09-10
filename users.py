class User():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.user_info = ''
        self.login_attempts = 0

    def describe_user(self):
        print(self.first.title() + " " + self.last.title() + " is a " +
              self.user_info + ".")

    def greet_user(self, greet_words):
        print("Hello, " + self.first.title() + " " + self.last.title() + ", "
                                                                    "" + greet_words)

    def increment_login_attempt(self):
        self.login_attempts += 1

    def set_login_attemp(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privilege()


class Privilege():
    def __init__(self):
        self.privilege = []
    def show_privileges(self):
        privilege = ['can add post', 'can delete post', 'can be user']
        print(privilege)

admin01 = Admin('liu', 'wei')
admin01.privileges.show_privileges()
