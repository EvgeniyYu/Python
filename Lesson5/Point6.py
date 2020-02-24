d = dict()

with open('point6.txt', 'r') as f:
    for line in f:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        line_elements = line.split('\t')
        s = 0
        for element in line_elements:
            pos = element.find('(')
            value = element[0: pos]
            if value.isdigit():
                s += int(value)
        d[line_elements[0]] = s
    print(d)