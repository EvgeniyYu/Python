from functools import reduce
from random import randint


numbers_list = [el * randint(0, 100) for el in range(10)]
print(f'Initial list of numbers: {numbers_list}')
result_list = []
for i in range(len(numbers_list)):
    if i > 0:
        if numbers_list[i] > numbers_list[i - 1]:
            result_list.append(numbers_list[i])

print(f'Result list of numbers: {result_list}')


