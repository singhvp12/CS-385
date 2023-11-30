# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder method


# Parent class 2
class Flyable:
    def fly(self):
        print(f"{self.name} is flying.")


# Parent class 3
class Swimmable:
    def swim(self):
        print(f"{self.name} is swimming.")


# Child class inheriting from Animal and Flyable
class Bird(Animal, Flyable):
    def make_sound(self):
        print(f"{self.name} is chirping.")


# Child class inheriting from Animal and Swimmable
class Fish(Animal, Swimmable):
    def make_sound(self):
        print(f"{self.name} is bubbling.")


if __name__ == "__main__":
    # Example usage
    bird = Bird("Sparrow")
    bird.make_sound()
    bird.fly()

    print()

    fish = Fish("Goldfish")
    fish.make_sound()
    fish.swim()
