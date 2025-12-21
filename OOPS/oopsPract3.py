# Getter and setter methods in Python

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative.")
        else:
            self._age = value   

dog1 = Dog("Buddy", 3)
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3

dog1.age = -5     # Output: Age cannot be negative.
dog1.age = 4
print(dog1.age)   # Output: 4
dog1.name = "Tiger"
print(dog1.name)  # Output: Tiger