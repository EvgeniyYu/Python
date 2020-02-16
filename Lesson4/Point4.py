from random import randint
list_numbers = [el * randint(0, 5) for el in range(20)]
print(f'Initial list: {list_numbers}')
result_numbers = [el for el in list_numbers if list_numbers.count(el) == 1]
print(f'Result list: {result_numbers}')