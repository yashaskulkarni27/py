# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    # def speak(self):
    #     pass  # This method will be overridden in the child classes

# Child class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"
    pass

# Child class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Creating objects of the child classes
dog = Dog("Fido")
cat = Cat("Whiskers")

# Calling the speak method
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

