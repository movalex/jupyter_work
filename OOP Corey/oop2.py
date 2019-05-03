# Python OOP2

class Employee():
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)
emp1 = Employee('Corey', 'Shchafer', 20000)
emp2 = Employee('Test', 'User', 45000)
# print(emp1)
# emp1.first = 'Corey'
# emp1.last = 'Schafer'
# emp1.email = 'fdjhgkd@gmail.com'
# emp1.pay = 20000
# print(emp1.email)
# print(emp2.email)
# print(Employee.fullname(emp1)) # this
# print(emp1.fullname())  # equals this
# print(emp1.pay)
# Employee.raise_amount = 1.05
# emp1.apply_raise()
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# 
# print(emp1.pay)
# emp2.raise_amount = 1.08
# 
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# 
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(Employee.__dict__)
print(Employee.num_of_emps)



