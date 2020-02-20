rating_list = [20, 15, 10, 5]
print(rating_list)
while True:
    try:
        val = int(input('Enter new element or (enter a symbol to exit): '))
        rating_list.append(val)
        rating_list.sort(reverse = True)
        print(rating_list)
    except ValueError:
        print('Exit')
        break