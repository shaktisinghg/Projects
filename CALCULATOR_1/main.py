
try:
    a = int(input('Inter number first:- '))
    b = int(input('Inter number first:- '))

    print('What operation you want to do.\npress + for add,\npress - for sub,\npress * for multiply\npress / for divide.')

    o = input('inter operation here:- ')

    match o:
        case '+' : 
            print(f'The result is {a + b}')
        case '-' : 
            print(f'The result is {a - b}')
        case '*' : 
            print(f'The result is {a * b}')
        case '/' : 
            print(f'The result is {a / b}')


except Exception as e:
    print(f"Error occured is {e}")


