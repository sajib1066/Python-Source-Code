class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(self.name, self.age)

person = Person('Sajib', 19)
person.details()

print('Name: ', person.name)
print('Age: ', person.age)
