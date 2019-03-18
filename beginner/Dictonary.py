#Dictionary

dict = {}

dict['name'] = 'sajib'
dict['age'] = 19

print(dict['name'], dict['age'], sep=' | ')

dict1 = {'Sajib' : 226758, 'Atik' : 226738, 'Tanim' : 226714}

#iterate
for name, roll in dict1.items():
    print(name, roll, sep=' | ')

#add new item
dict1['Pabel'] = 226745

print(dict1)

#delete item
del dict1['Atik']
print(dict1)
