#object oriented programming


from ossaudiodev import SNDCTL_SYNTH_CONTROL
from unicodedata import name


My_employee = {
    'name': 'random name',
    'grades': [234,88,90],
}

def avrg_grade(Employee):
    return sum(Employee['grades']) / len(Employee['grades'])
 
print(avrg_grade(My_employee))

# object that stores data
# class defines object
#define function in class - dunder function

#here you have defined object and structure
class Employee: 
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade
    
    def average(self):
        return sum(self.grade) / len(self.grade)

#create object

Employee_one = Employee('Name of employee 1', [33,66,99])
Employee_two = Employee('Name of employee 2', [100,99,1])

print(Employee_one.__class__)
print(Employee_two.name)
print(Employee_one.average())

# len(my-list) = length of my_list (works with tupples and strings)
# max(my_list) = maximum number in my_list
# round(my_decimal) = rounds my_decimal


#Parameter naming in python

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

Matrix = Movie('The Matrix', 1994)
print(Matrix.name)

# magic methods in python
# if we make a list into an object, anything in the list-object we can use the same commands e.g. Len

class Student:
    def __init__(self, name):
        self.name = name

movies = ['Matrix', 'Finding Nemo']
print(len(movies))

class garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
        
    def __repr__(self):
        return f'<garage {self.cars}>'
    def __str__(self):
        return f' <garage with {len(self)} cars>'

# repr is for debugging
# str is more user friendly

ford = garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')


for car in ford:
    print(ford)

#magic methods in python --- repetition

class student:
    def __init__(self, name):
        self.name = name

movies = ['matrix','finding nemo']
print(movies.__class__)
print('hi'.__class__)
print(len(movies))

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self)} cars.'

form = garage()
ford.cars.append('fiesta')
ford.cars.append('focus')

print(len(ford))
print(ford[0])
for car in ford:
    print(car)

print(ford)


## Inheritance in Python

class student: 
    def __init__(self):
        self.name = name
        self.marks = []
    
    
    def average(self):
        return sum(self.marks) / len(self.marks)

class workingstudent:
    def __init__(self, name, salary):
        self.name = name
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = workingstudent('rolf', 15.50)
print(rolf.salary)

