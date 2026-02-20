name = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления: ')
with open('sensor_log.txt', 'w', encoding='utf-8') as report:
    report.write(f'Оператор:\t{name}\n')
    report.write(f'Давление:\t{pressure}')
print('Данные успешно сохранены в sensor_log.txt')