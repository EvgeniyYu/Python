data_list = []
index = 0
while True:
    str_name = input('Enter the name of the product: ')
    str_price = input('Enter the price: ')
    str_count = input('Enter the number of products: ')
    str_measure = input('Enter the measure: ')
    param_dict = {'name': None, 'price': None, 'count': None, 'measure': None}
    product_tuple = ('index', param_dict)
    param_dict['name'] = str_name
    param_dict['price'] = str_price
    param_dict['count'] = str_count
    param_dict['measure'] = str_measure
    index += 1
    product_tuple = (index, param_dict)
    data_list.append(product_tuple)
    if input("input 'ok' to show results or press any symbol to continue: ") == 'ok':
        break

print(f'You entered the next data: {data_list}')

my_dict = {'name': [], 'price': [], 'count': [], 'measure': []}
list_names = []
list_prices = []
list_count = []
list_unit = []
for record in data_list:
    list_names.append(record[1].get('name'))
    list_prices.append(record[1].get('price'))
    list_count.append(record[1].get('count'))
    list_unit.append(record[1].get('measure'))
my_dict['name'] = list_names
my_dict['price'] = list_prices
my_dict['count'] = list_count
my_dict['measure'] = list_unit
print(my_dict)
