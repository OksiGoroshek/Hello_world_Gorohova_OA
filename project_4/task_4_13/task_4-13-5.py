n = int(input('Сколько чисел будем сравнивать?'))

maximum = 0
i = 1

while n >= i:
    N = float(input('Введите число: '))
    if N > maximum:
        maximum = N
    i = i + 1
print(maximum)