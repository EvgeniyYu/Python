month_num = 0
while True:
    try:
        month_num = int(input('Enter the number of month (1-12): '))
        if month_num <= 0 or month_num > 12:
            print('Error! The value must be inside the interval from  1 to 12')
            continue
    except ValueError:
        print('Error! You should input the integer value')
        continue
    break


#using dictionary to define the season
month_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
              9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
season_name = month_dict.get(month_num)
print(f'Month {month_num} is {season_name}')


#using tuple to define the season
#season tuples
winter_tuple = (1, 2, 12)
spring_tuple = (3, 4, 5)
summer_tuple = (6, 7, 8)
autumn_tuple = (9, 10, 11)

if winter_tuple.__contains__(month_num):
    print(f'Month {month_num} is Winter')
elif spring_tuple.__contains__(month_num):
    print(f'Month {month_num} is Spring')
elif summer_tuple.__contains__(month_num):
    print(f'Month {month_num} is Summer')
elif autumn_tuple.__contains__(month_num):
    print(f'Month {month_num} is Autumn')
