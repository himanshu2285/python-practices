class Person:
    eye_color = "black"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Eye Color: {self.eye_color}"
    
boy = Person("Jimmy", 12)
teen = Person("Andrew", 16)
adult = Person("John", 25)
print(boy)
print(teen)
print(adult)
