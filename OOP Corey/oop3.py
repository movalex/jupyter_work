# Python OOP3 classmethods
import datetime

class Employee:
    '''test'''
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """parse name and pay from string"""
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """check of ot os a workday"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False, 'today is not a workday'
        return True, 'today is a workday' 

emp1 = Employee('Corey', 'Shchafer', 20000)
emp2 = Employee('Test', 'User', 45000)

my_date = datetime.date(2019,3,12)
print(Employee.is_workday(my_date))
print(Employee.is_workday(datetime.datetime.today()))


emp_str_1 = 'John-Doe-70000' 
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_1.fullname())

first, last, pay = emp_str_1.split('-')
print(first)

#  use classmethod:
Employee.set_raise_amt(1.05)
#  the same would be:
Employee.raise_amt = 1.05

#  we can evem run this classmethod from the instance,
#  and it still changes raise_amt for whole class:
#  emp1.set_raise_amt(1.05) 
#  but this does not make sense

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)





