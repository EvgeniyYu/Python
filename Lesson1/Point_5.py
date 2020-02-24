income = int(input('Enter the income: '))
expenses = int(input('Enter the expenses: '))
if income > expenses:
    print('Income is more than expenses: difference is %d' % (income - expenses))
    persons_count = int(input('Enter the number of persons: '))
    print('Personal income is %f' % float((income - expenses)/persons_count))
else:
    print('Expenses are more than income: difference is %d' % (income - expenses))