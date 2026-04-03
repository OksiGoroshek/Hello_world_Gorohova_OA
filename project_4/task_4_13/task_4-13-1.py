A = float(input("Введите число A:"))
B = float(input("Введите число B:"))
C = float(input("Введите число C:"))
D = float(input("Введите число D:"))

if A < D:
    if A < C:
        if A < B:
            Minimum = A
        else:
            Minimum = B
    else:
        if C > B:
            Minimum = B
        else:
            Minimum = C
else:
    if D > C:
        if C > B:
            Minimum = B
        else:
            Minimum = C
    else:
        if D > B:
            Minimum = B
        else:
            Minimum = D

print(Minimum)