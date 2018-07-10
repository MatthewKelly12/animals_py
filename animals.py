class Animal():
    """This represents an animal"""

    def __init__(self, species, animal_noise):
        self.species = species
        self.animal_noise = animal_noise

    def speak(self):
        """Returns the name of the company"""

        return print(f'I am a {self.species} and I say {self.animal_noise}')


