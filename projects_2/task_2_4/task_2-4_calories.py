proteins = int(input('Масса белков в продукте (г): '))
fats = int(input('Масса жиров в продукте (г): '))
carbohydrates = int(input('Масса углеводов в продукте (г): '))
calorie_content = proteins*4 + fats*9 + carbohydrates*4
print(f'Общая калорийность: {calorie_content}')