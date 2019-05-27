game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(' 0, 1, 2')
for count, row in enumerate(game, start=1):
    print(count, row)
    for n, item in enumerate(row, start=1):
        print('     {} = {}'.format(n, item))

li = ['sajib', 'atik', 'toufiq', 'sheme']
print(list(enumerate(li, start=1)))

for c, i in enumerate(li, start=1):
    print(c, i)
