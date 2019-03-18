class Resturant():
    name = ''
    owner = ''
    def details(self):
        print(self.name, self.owner)
    def resturant_address(self, address):
        print(self.name, self.owner)
        print(address)


resturant = Resturant()
resturant.name = 'Doi Ghor'
resturant.owner = 'Sajib'
resturant.details()
resturant.resturant_address('Jessore')
