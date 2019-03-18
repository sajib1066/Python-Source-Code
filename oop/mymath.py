def sum(x, y):
    return x + y

def min(x, y):
    return x - y

class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y
    def min(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
