str = input('Enter the string: ')
words = list(str.split(' '))
for i in range(len(words)):
    if len(words[i]) > 10:
        print(f'{i}: {(words[i])[0: 10]}')
    else:
        print(f'{i}: {words[i]}')

