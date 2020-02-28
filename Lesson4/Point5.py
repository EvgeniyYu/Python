from functools import reduce
def multiply(p1, p2):
    return p1 * p2

list_numbers = [el for el in range(100, 1001) if el % 2 == 0]
print(list_numbers)
print(reduce(multiply, list_numbers))