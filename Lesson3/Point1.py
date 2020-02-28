divide = lambda p1, p2: p1 / p2

val_1 = 0
val_2 = 0
cnt = 0;
while True:
    try:
        if cnt == 0:
            val_1 = int(input('Enter the first value: '))
            cnt += 1

        if cnt == 1:
            val_2 = int(input('Enter the second value: '))
            if val_2 == 0:
                print('Second value cannot be zero')
                continue
            cnt += 1

        if cnt == 2:
            print(f'Result of {val_1} / {val_2} is {divide(val_1, val_2)}')
            break
    except ValueError:
        print('Symbol must be an integer value!')


