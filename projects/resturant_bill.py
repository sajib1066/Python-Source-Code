a = int(input('Enter your resturent bill amount: '))
b = a
#Block for 1000......................
temp = a // 1000
print(temp, '1000 Taka note(s).')
if temp > 0:
    a = a % 1000
    b = a
else:
    a = b
#Block for 500......................
temp = a // 500
print(temp, '500 Taka note(s).')
if temp > 0:
    a = a % 500
    b = a
else:
    a = b
#Block for 100......................
temp = a // 100
print(temp, '100 Taka note(s).')
if temp > 0:
    a = a % 100
    b = a
else:
    a = b
#Block for 50.......................
temp = a // 50
print(temp, '50 Taka note(s).')
if temp > 0:
    a = a % 50
    b = a
else:
    a = b
#Block for 20.......................
temp = a // 20
print(temp, '20 Taka note(s).')
if temp > 0:
    a = a % 20
    b = a
else:
    a = b
#Block for 10......................
temp = a // 10
print(temp, '10 Taka note(s).')
if temp > 0:
    a = a % 10
    b = a
else:
    a = b
#Block for 5.......................
temp = a // 5
print(temp, '5 Taka note(s).')
if temp > 0:
    a = a % 5
    b = a
else:
    a = b
#Block for 2.......................
temp = a // 2
print(temp, '2 Taka note(s).')
if temp > 0:
    a = a % 2
    b = a
else:
    a = b
#Block for 1......................
temp = a // 1
print(temp, '1 Taka koen(s).')

