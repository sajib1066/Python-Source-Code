num = [1,2,3,4,5,6,7,8,9,10, 'math', 6.7]

#adding list item
sum = 0
for i in num:
    if type(i) == int:
        sum += i
    print(i)

print('Sum is {sum}'.format(sum=sum))

car_list = ['honda', 'hino', 'toyota', 'tata']

#adding list
car_list.append('bmw')
print(car_list)

#insert
car_list.insert(2, 'ak')
print(car_list)

#delete
del car_list[2]
print(car_list)

#pop last item
last_car = car_list.pop()
print(car_list,'\n',last_car)

#remove
car_list.remove('tata')
print(car_list)

#string to list convert
cars = 'honda, bmw, tata, toyota, hino'
print(type(cars), ' : ',cars)

import re
car_list_2 =  re.split(',', cars)
print(type(car_list_2), ' : ',car_list_2)

#list to string convert
qoute = ['i', 'love', 'my', 'country']
print(qoute)
qoute_str = ' '.join(qoute)
print(qoute_str)

#sorting list
print(car_list_2)
car_list_2.sort(reverse=True)
print(car_list_2)
print(sorted(car_list_2))
print(car_list_2)
