a = [7, 3, 8, 1, 4, 6, 2, 5]
n = len(a)

i = 0
Summa = 0
Sr = 0

while i < n:
    Summa = Summa + a[i]
    i = i + 1

Sr = Summa / n

print(Sr)