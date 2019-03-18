def div(x, y):
    try:
        result = x / y
    except Exception as e:
        print('Error Type: ', e)
        return None
    else:
        print('Division is: ', result)
    finally:
        print('.........Execute Finallay Block!.............')
        result = None
        print(result)

div(4, 0)
div('4', '2')
div(10, 2)
