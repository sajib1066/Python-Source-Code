#Tupple

tp = (1, 2, 3)
print(tp, type(tp))
#iterate
for t in tp:
    print(t)

#comapre
tp1 = (1,3,2)
tp2 = (1,2,3)
if tp1 == tp2:
    print('Same Value!')
else:
    print('Not Same!')

#packing
x, y, z = 5, 6, 7
tp3 = (x,y,z)
print(tp3)

#Unpacking
tp4 = (1,2,3)
x, y , z = tp4

print(x, y, z, sep=' | ')
