from animals import Animal

class Dog(Animal):
    """This component defines a dog"""

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
        super().__init__("dog","woof")

    def bark(self):
        return (Animal.speak(self))









