# Python OOP5 special methods

import datetime

class Employee:
    '''test'''
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return f'{self.fullname()} - {self.email}' 
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Corey', 'Shchafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1) # returns __str__
print(repr(emp1))
print(emp1.__repr__())
print(emp1.__str__())

print(int.__add__(1,2))
print(emp1 + emp2)

print(len('test'))
print('test'.__len__())
print(len(emp1.fullname()))
