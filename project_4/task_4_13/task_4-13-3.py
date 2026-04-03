N = int(input('Введите число: '))

i = 1
factorial = 1

while i <= N:
    factorial = factorial * i
    i = i + 1

print(factorial)