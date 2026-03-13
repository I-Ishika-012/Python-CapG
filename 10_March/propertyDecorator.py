'''
Property Decorator
'''

class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation
    
    def display(self):
        print(f"Name: {self._name}, Age: {self._age}, Gender: {self._gender}, Occupation: {self._occupation}")
        
person = Person("John", 25, "Male")
person.occupation = "Engineer"
person.display()
   