class Dog:
    @staticmethod
    def info():
        return "Dogs are loyal animals."
    
    
    @classmethod
    def species(cls):
        return "Canis lupus familiaris"

# 1st method call
print(Dog.info())          # Output: Dogs are loyal animals.
print(Dog.species())       # Output: Canis lupus familiaris

# 2nd method call
dog1 = Dog()
print(dog1.info())         # Output: Dogs are loyal animals.
print(dog1.species())      # Output: Canis lupus familiaris