n = input('Enter number: ')
i = 0
str = ''
s = 0
while i < 3:
    str += n
    s += int(str)
    i += 1
print('Result: %d '% s)