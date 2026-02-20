environment = input('Введите название питательной среды: ')
concentration = input('Введите концентрацию агара: ')
temperature = input('Введите температуру стериализации: ')
with open('recipe.txt', 'w', encoding='utf-8') as card:
    card.write(f'{environment.upper()}\n Концентрация: {concentration}\n Температура: {temperature}')
print('Файл "recipe.txt" успешно сформирован!')