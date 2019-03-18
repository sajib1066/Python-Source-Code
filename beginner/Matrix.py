matrix = [
    [1,2,3,4,5],
    [5,6,0,1,2],
    [0,5,3,1,9],
    [2,8,9,0,1]
]

for x in matrix:
    for y in x:
        print(y, end = ' ')
    print()

print(matrix[1][1])
