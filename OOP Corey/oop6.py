# Python OOP6 special methods


class Employee:
    '''special methods sample'''
    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('delete name!')
        self.first = None
        self.last = None


emp1 = Employee('John', 'Smith')
emp1.first = '222Jim'  # email does not change
print(emp1.first)
emp1.fullname = 'corey schafer'  # can't set attribute, we need a setter

print(emp1.first)
print(emp1.email)
''' with @property we cal call
method as attribute, its a getter,
it becomes string instead of object'''
print(emp1.email)
print(emp1.fullname)

# property defines a method but we can assess it like an attribute

del emp1.fullname
print(str(emp1.first) + ', there\'s no name anymore')
