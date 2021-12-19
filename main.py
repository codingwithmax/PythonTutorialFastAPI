class Animal:
    friends = []

    def __init__(self, height=100, weight=100):
        self.height = height
        self.weight = weight
        self._private_weight = 50
        self.__very_private_weight = 30

    def print_height(self):
        print(f"This animal's height is: {self.get_height()}")

    def get_height(self):
        return self.height

    def get_fur_colour(self):
        return self.fur_colour

    def get_friends(self):
        return self.friends

    def set_height(self, height):
        self.height = height

    def greet(self):
        print("This animal makes no sound")


class Dog(Animal):
    def __init__(self, height, weight, fur_colour):
        self.fur_colour = fur_colour
        super().__init__(height=height, weight=weight)

    @classmethod
    def greet(self):
        print("Woof, woof")


class Config:
    RATE_LIMIT = ...
    HOST_URL = ...


sample_dog = Dog(50, 25, "brown")
print(sample_dog.fur_colour, sample_dog.height)
sample_dog.print_height()
sample_dog.greet()

Dog.greet()
print("A dog's starting friends are:", Dog.height)
