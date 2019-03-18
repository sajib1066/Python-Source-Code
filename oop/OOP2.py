class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(self.name, self.age, sep='|')

person_list = []
for i in range(0,10):
    person = Person('person'+str(i), 18+i)
    person_list += [person]

for x in person_list:
    x.details()
