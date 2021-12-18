class Animal:
    fur_colour = "grey"
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


animal_1 = Animal(height=120, weight=80)
animal_2 = Animal(height=70, weight=150)
animal_3 = Animal()

animal_1.print_height()

print(animal_2.get_height())

print(animal_3.height)

print(animal_1.friends, animal_2.get_friends())
animal_3.friends.append("Jerry")

print(animal_1.friends, animal_2.get_friends())


print(animal_3.height)
animal_3.set_height(90)
print(animal_3.height)

print(animal_3._private_weight)
print(animal_3.__very_private_weight)
