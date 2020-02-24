str = input('Enter elements of a list using separator (,): ')
my_list = str.split(',')
print(my_list)
for i in range(len(my_list)):
    if i % 2 != 0:
        continue
    if i < len(my_list) - 1:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(f'Result: {my_list}')
