# Python OOP

class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Corey', 'Shchafer', 20000)
emp2 = Employee('Test', 'User', 45000)

# print(emp1)
# print(emp2)

# emp1.first = 'Corey'
# emp1.last = 'Schafer'
# emp1.email = 'fdjhgkd@gmail.com'
# emp1.pay = 20000

# emp2.first = 'test'
# emp2.last = 'User'
# emp2.email = 'fgkhdfgk@jhgfjfd.com'
# emp2.pay = 40000

print(emp1.email)
print(emp2.email)

print(Employee.fullname(emp1)) # this
print(emp1.fullname())  # equals this

