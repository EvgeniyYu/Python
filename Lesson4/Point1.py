from sys import argv

calc_month_salary = lambda hours, salary_hour, award: hours * salary_hour + award

try:
    script_name, hours, salary_hour, award = argv
    print(f'Input data are: script_name = {script_name}  hours = {hours}  salary_hour = {salary_hour}  award = {award}')
    month_salary = calc_month_salary(int(hours), int(salary_hour), int(award))
    print(f'Month salary is {month_salary}')
except ValueError:
    print('You should input 3 integer parameters: hours, salary per hour and award')