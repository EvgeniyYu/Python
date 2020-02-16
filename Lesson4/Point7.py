def gen(n):
   for el in range(n):
       yield el + 1

def fact(n):
    x = 1
    for el in gen(n):
        x *= el
    return x

while True:
    try:
        val = int(input('Input the number to calculate the factorial: '))
        if val < 0:
            print('You should input a positive integer value')
        else:
            print(f'The factorial of {val} is {fact(val)}')
            break
    except ValueError:
        print('You should input an integer value!')
