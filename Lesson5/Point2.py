try:
    f = open('user_data.txt', 'r')
    lines = f.readlines()
    cntLines = len(lines)
    print(f'Number of lines is {cntLines}')
    for line in lines: print(len(line))
    f.close()
except IOError:
    print('File cannot be open')
