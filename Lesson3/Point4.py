my_func = lambda x, y: x ** y

def my_func2(x, y):
    res = 1
    for i in list(range(abs(y))):
        if y < 0:
            res *= (1/x)
        else:
            res *= x
    return res

val_1 = 0
val_2 = 0
cnt_val = 0
while True:
    try:
        if cnt_val == 0:
            val_1 = int(input('Enter a positive integer value: '))
            if val_1 < 0:
                print('Value must be positive')
                continue
            cnt_val += 1

        if cnt_val == 1:
            val_2 = int(input('Enter a negative integer value: '))
            if val_2 >= 0:
                print('Value must be negative')
                continue
            break
    except ValueError:
        print('Value must be integer!')

print(f'Result is {my_func(val_1, val_2)}')