"""
1.
class Laptop:
    Make the class with composition.
class Battery:
    Make the class with composition.
    """
class Laptop:
    def __init__(self):
        main_battery = Battery('This is stuff of main battery')
        reserve_battery = Battery('This is stuff of reserve battery')
        self.battery = [main_battery, reserve_battery]

class Battery:
    def __init__(self, energy):
        self.energy = energy

laptop = Laptop()

""" 
2.
class Guitar:
    Make the class with aggregation
class GuitarString:
    Make the class with aggregation
    """
class Guitar:
    def __init__(self, string):
        self.string = string

class GuitarString:
    def __init__(self):
        pass

mstring = GuitarString()

"""3
class Calc:
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note:this method should be static
    """
class Calc:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3

print(Calc.add_nums(1, 2, 3))

"""4
class Pasta:
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs'] """









"""6.
class AddressBookDataClass:
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), 
                                    address (str), email (str), birthday (str), age (int)"""

import dataclasses
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

my_adress = AddressBookDataClass(key='iron', name='Olena', phone_number='01', address='Kyiv', email='o.la@gmail', birthday='12', age=20)
print(my_adress)

"""7. Create the same class (6) but using NamedTuple"""
from collections import namedtuple
my_adress = namedtuple('my_address',['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'] )
m_address = ('iron', 'Olena', '01', 'Kyiv', 'o.la@gmail', '12', '20')
print("This is my address", end=" ")
print(m_address)

"""8.
class AddressBook:
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
    def descrading (self):
        print(f"m_address2 (key= '{self.key}', name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', email='{self.email}', birthday='{self.birthday}', age='{self.age}' )")

m_address2 = AddressBook('iron', 'Olena', '01', 'Kyiv', 'o.la@gmail', '12', '20')
print(m_address2.descrading())

"""
9.
class Person:
    Change the value of the age property of the person object
    name = "John"
    age = 36
    country = "USA" """
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.__age = age
        self.country = country

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

person1 = Person('John',36,'USA')
person1.age = 37
print(person1.age)

"""10.
class Student:
   
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    id = 0
    name = 
    def __init__(self, id, name):
        self.id = id
        self.name = name"""

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

s = Student(8, 'Ben')
setattr(s, 'email', 'ben@gmail.com')
print("The Ben's email is", s.email)
setattr(s, 'new email', 'boba@gmail')
print(getattr(s, "new email"))

"""11
class Celsius:
    
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)

    def __init__(self, temperature=0):
        self._temperature = temperature

# create an object
{obj} = ...

print({obj}.temperature)"""
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature_to_F(self):
        return self._temperature*1.8 + 32

    @temperature_to_F.setter
    def temperature_to_F(self, value):
        self._temperature = value

obj = Celsius (10)
obj.temperature_to_F = 100
print(obj.temperature_to_F)