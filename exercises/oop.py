# demontration of OOP concepts in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
def demonstrate_oop():
    """Demonstrates OOP concepts with Animal, Dog, and Cat classes."""
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    print(dog.speak())
    print(cat.speak())

if __name__ == "__main__":
    demonstrate_oop()