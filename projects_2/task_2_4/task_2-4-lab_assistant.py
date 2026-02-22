volume = float(input('Нужный объем раствора (в мл): '))
salt_mass = round(volume*0.009, 2)
border = '-'*23+'\n'

with open('recipe.txt', 'w', encoding='utf-8') as report:
    report.write('ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n')
    report.write(border)
    report.write(f'Общий объем: {volume} мл\nМасса соли: {salt_mass} г\nОбъем воды: {volume} мл')