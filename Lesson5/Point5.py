num_list = []
str = input('Enter  the numbers separated with spaces: ')
str_nums = str.split(' ')
for val in str_nums:
    if val.isdigit() == True:
        num_list.append(val)

with open('point5.txt', 'w') as f:
    f.write(' '.join(num_list))

with open('point5.txt', 'r') as f:
    num_list = []
    s = 0
    for line in f:
        num_list = line.split(' ')
        for num in num_list: s += int(num)
    print(f'Sum of all numbers is {s}')