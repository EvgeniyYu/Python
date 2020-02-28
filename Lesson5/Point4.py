def getRusVal(sEN):
    sEN = sEN.replace(' ', '')
    if sEN == 'One':
        return 'Один'
    elif sEN == 'Two':
        return 'Два'
    elif sEN == 'Three':
        return 'Три'
    elif sEN == 'Four':
        return 'Четыре'
    else:
        return ''

res = []
try:
    with open('point4.txt') as f:
        for line in f:
            l = list(line.split('-'))
            res.append(getRusVal(l[0]) + ' - ' + str(l[1]))
    with open('point4_ru.txt', 'w') as f:
        for line in res:
            f.write(line)


except IOError:
    print('File cannot be open')