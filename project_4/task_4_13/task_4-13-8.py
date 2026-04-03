a = [7, 3, 8, 1, 4, 6, 2, 5]
n = len(a)

i = 0
c = 0

while i < n:
    if a[i] > 0:
        c = c + 1
    i = i + 1

print(c)