a = int(input('Enter a: '))
b = int(input('Enter b: '))
x = a/10
i = 1
print('Day: %d  Distance: %d km' % (i, a))
while a < b:
    a += x
    x = a / 10
    i += 1
    print('Day: %d  Distance: %f km' % (i, a))
print('The man will run %d km in %d days' % (b, i))