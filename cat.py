from animals import Animal

class Cat(Animal):
    """This component defines a Cat"""

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
        super().__init__("cat", "meow")

    def meow(self):
        return (Animal.speak(self))









