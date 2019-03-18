class X:
    def __init__(self, name):
        self.name = name
        print(self.name, 'is created...................!')
    def __del__(self):
        print(self.name, 'is deleted...................!')

x = X('.................x')
y = X('.................y')
print('Hello mnds')

def hello():
    x = X('mnds')
    y = X('sajib')
    print(x.name, y.name)

hello()
