def findPosLetter(value_list):
    letters_list = list(filter(lambda x: x.isalpha(), value_list))
    try:
        return value_list.index(letters_list[0] if len(letters_list) > 0 else -1)
    except:
        return -1

s = 0
to_exit = False
print('Enter any letter to exit')
while True:
    val_input = input('Enter the sequence of numbers separated with space: ')
    val_list = val_input.split()
    posLetter = findPosLetter(val_list)
    if posLetter >= 0:
        val_list = val_list[0: posLetter]
        to_exit = True
    try:
        s += (lambda val_list: sum(list(map(int, val_list))))(val_list)
        print(s)
        if to_exit:
            break
    except:
        print('Exception error')
        break