#define a function

def hello(name):
    print('Hello {}, how are you?'.format(name))

hello('Sajib')

#positional argument

def person_details(name, age, country = 'Bangladesh'):
    print('Name: {}\nAge: {}\nCountry: {}\n'.format(name, age, country))

person_details('Sajib', 19, 'Bangladesh')
person_details('Rashed', 19)

person_details(name = 'Sajib', age = 19, country = 'Germany')

#return value

def square(num):
    return num * num

print(square(2), square(4.4), sep = ' | ')

def get_name(first_name, last_name, middle_name = ''):
    complete_name = first_name
    if middle_name:
        complete_name += ' ' + middle_name
    complete_name += ' ' + last_name
    return complete_name

print(get_name('Sajib', 'Hossain'))
print(get_name('Md', 'Hossain', 'Sajib'))


#value type parameter

num = 100

def change_num(num):
    num += num
    print(num)

change_num(num)
print('Function out Num: {}'.format(num))

#referance type parameter

my_list = [1, 2, 3, 4, 5]
my_dict = {'one':1, 'two':2, 'three':3}

def change_list_dict(list, dict):
    del list[0]
    list[-1] = 100

    del dict['one']
    dict['three'] = 33

    print('Inner Function list: ', list)
    print('Inner Function dict: ', dict)

print('Before Function Calling...')
print(my_list)
print(my_dict)
change_list_dict(list = my_list, dict = my_dict)

print('After Function Calling....')
print(my_list)
print(my_dict)

#arbitary arguments

def students(*students_name):
    for student in students_name:
        print(student)

students('Sajib', 'Pabel', 'Tanim', 'Atik')
students()
students('Sajib')

#positional and arbitary mixing

def student(captain, *other_student):
    print('Captain: ', captain)
    print('Other Student: ', other_student)

student('Sajib', 'Atik', 'Tanim')

# * means tuple
# ** means dictionary

#arbitary and keyword arguments

def Student(captain, **other_student):
    print('Captain: ', captain)
    print('Other Student: ', other_student)

Student(captain = 'Sajib', second_captain = 'Atik', third_captain = 'Tanim')

# lambda

add_number = lambda x, y: x + y

print(add_number(3, 5))

bd_public = lambda name: 'Bangladeshi Citizen: '+ name
print(bd_public('Sajib Hossain'))
