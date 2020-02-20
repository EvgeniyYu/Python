try:
    f = open('point3_users.txt', 'r')
    lines = f.readlines()
    msal = 0
    for line in lines:
        l = line.split()
        msal += int(l[1])
        if int(l[1]) < 20000: print(l[0])
    print(f'Medium salary is {msal/len(lines)}')
    f.close()
except IOError:
    print('Cannot open file')