from itertools import count, cycle
start_el = 3
end_el = 10
cnt = 20
list_numbers = []
for el in count(start_el):
    if el > end_el:
        break
    else:
        list_numbers.append(el)
print(f'First list: {list_numbers}')
cycle_list =[]
for el in cycle(list_numbers):
    cycle_list.append(el)
    cnt -= 1
    if cnt == 0:
        break
print(f'Cycle list: {cycle_list}')

