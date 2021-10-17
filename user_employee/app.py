class Employee:
    def __init_(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def display(self):
        return f'{self.firstname} {self.lastname}'

    @classmethod
    def user_input(cls):
        while True:
            try:
                firstname = input('Enter first name: ')
                lastname = input('Enter last name: ')
                return self(firstname, lastname)
            except:
                print('Oops...Invalid input!')
                continue

s = Employee.user_input()
s.display()
