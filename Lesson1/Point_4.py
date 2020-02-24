str = input('Enter the number: ')
i = 0
max_val = 0
while i < len(str):
    if int(str[i]) > max_val:
        max_val = int(str[i])
    i += 1
print('Maximal value of number %d is %d' % (int(str), max_val))
