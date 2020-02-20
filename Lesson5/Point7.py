import json

d_firms = dict()
d_profit = dict()
list_results = list()

with open('point7.txt') as f:
    s = 0
    for line in f:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        list_values = line.split('\t')
        try:
            list_values.remove('')
        except:
            pass
        print(list_values)

        name = ''
        ownership = ''
        income = 0
        expense = 0
        for j in enumerate(list_values):
            i = j[0]
            if i == 0:
                name = list_values[i]
            elif i == 1:
                ownership = list_values[i]
            elif i == 2:
                income = list_values[i]
            elif i == 3:
                expense = list_values[i]
                d_firms[name] = int(income) - int(expense)
                s += int(income) - int(expense)
            else:
                continue

d_profit["average_profit"] = s/len(d_firms)
print(d_firms)
print(d_profit)
list_results.append(d_firms)
list_results.append(d_profit)
print(list_results)

with open('point7_result.txt', 'w') as f:
    json.dump(list_results, f)