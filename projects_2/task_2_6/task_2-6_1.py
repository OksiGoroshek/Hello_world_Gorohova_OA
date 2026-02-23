pH = float(input('Введите значение pH: '))
if pH > 7:
    print('Среда щелочная')
elif pH < 7:
    print('Среда кислая')
else:
    print('Среда нейтральная')