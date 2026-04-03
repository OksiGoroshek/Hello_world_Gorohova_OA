a = [7, 3, 8, 1, 4, 6, 2, 5]
n = len(a)

i = 0
Summa = 0

while i < n:
    if a[i] % 2 == 0:
        i = i + 1
    else:
        Summa = Summa + a[i]
        i = i + 1

print(Summa)