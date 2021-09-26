# 5 задание посчитать фин результат компании
revenue = int(input('Выручка: '))
expense = int(input('Издержки: '))

if revenue >= expense:
    profit = revenue - expense
    print('прибыль: ', profit)
else:
    revenue < expense
    loss = revenue - expense
    print('убыток: ', loss)

if revenue > expense:
    return_revenue = profit / revenue
    print('рентабельность: ', "%.2f" % return_revenue)

if revenue > expense:
    employees = int(input('количество сотрудников: '))
    print('прибыль на 1 сотрудника: ', "%.2f" % (profit / employees))

