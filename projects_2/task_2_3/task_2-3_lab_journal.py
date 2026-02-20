name = input('Введите ФИО: ')
data = input('Введите дату: ')
experiment = input('Введите имя эксперимента: ')
result = input('Введите выводы: ')
border = '+' + '-'*50 + '+\n'
width = 50
with open('journal.txt', 'w', encoding='utf-8') as report:
    report.write(border)
    report.write(f' Электронный лабораторный журнал\n')
    report.write(border)
    report.write(f' ФИО исследователя: {name}\n Дата: {data}\n Эксперимент: {experiment}\n')
    report.write(border)
    report.write(' Вывод:\n')
    for i in range(0, len(result), width): 
            report.write(f' {result[i:i+width]:<{width}}\n')
    report.write(border)