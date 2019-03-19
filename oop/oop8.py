#object comparison
x = [1, 2, 3, 4, 5]
xx = x
print(x == xx)
print(x is xx)

y = list(x)

print(y == x)
print(y is x)

