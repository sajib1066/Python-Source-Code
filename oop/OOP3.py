class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_name(self, name):
        self.name = name

    def details(self):
        print(self.name, self.age, sep = '|')

person = Person('Sajib', 19)
person.details()

person.name = 'Mnds'
person.details()

person.change_name('Mendis')
person.details()
