class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

class ExtMath (Math):
    def __init__(self, x, y):
        super().__init__(x, y)
    def min(self):
        return self.x - self.y

class MathDiv:  #Parent Class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def division(self):
        return self.x / self.y

class ExtMath1 (ExtMath, MathDiv):  #Child Class
    def __init__(self, x, y):
        super().__init__(x, y)

    def multiple(self):
        return self.x * self.y

    def sum(self):  #Method Overriding
        return self.x + self.y + 100

    def show_all(self):
        print('Parent/super class of Sum: ', super().sum())
        print('Child/sub class of Sum: ', self.sum())


calculate = ExtMath1(20,5)
print(calculate.sum())
print(calculate.min())
print(calculate.division())
print(calculate.multiple())

print()

calculate.show_all()
