f = open('user_data.txt', 'w')
while True:
    data = input('Enter data: ')
    if data == '':
        break
    else:
        f.write(data + '\n')
f.close()
