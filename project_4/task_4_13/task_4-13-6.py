n = int(input('Сколько чисел?'))

Summa = 0
i = 1

while n >= i:
    N = float(input('Введите число: '))
    Summa = Summa + N*N
    i = i + 1

print(Summa)