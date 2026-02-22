capsules = int(input('Введите общее количество произведенных капсул: '))
packing_capacity = int(input('Введите количество капсул в одной упаковке: '))
full_packaging = capsules // packing_capacity
surplus = capsules % packing_capacity

print(f'--- Отчет фасовочного цеха ---\nПолных упаковок:\t{full_packaging}\nОстаток капсул: \t{surplus}')