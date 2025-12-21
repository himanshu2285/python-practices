class Dog:
    color = "Brown"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def activity(self):
        return "running!"

obj = Dog("Buddy", 3)
print(obj.name)      # Output: Buddy
print(obj.age)       # Output: 3
print(obj.color)     # Output: Brown

print(obj.activity())