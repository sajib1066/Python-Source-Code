class Alien:
    legs = 5 # class variable
    def __init__(self, name):
        self.name = name # instant variable

    def __str__(self):
        return f'class name: {self.__class__.__name__}, object name: {self.name}'

alien1 = Alien('Montal')
alien2 = Alien('Vokkalada')

#Alien.legs = 100   # accessing class variable
alien1.__class__.legs = 50 # another way to accessing class variable

print(alien1.name, alien2.name)
print(alien1.legs, alien2.legs)
