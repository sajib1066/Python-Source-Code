try:
    with open('data/description.txt') as fobj:
        contents = fobj.read()
        print(contents)
except Exception as e:
    print(e)
