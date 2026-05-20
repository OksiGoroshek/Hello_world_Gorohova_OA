import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in df.columns[2:]:
    coef_var = (df[i].std() / df[i].mean()) * 100
    with open('task_6-0_7.txt', 'a', encoding='utf-8') as file:
        file.write(i)
        file.write(f'\nДисперсия: \t {df[i].var():.1f}')
        file.write(f'\nСтандартное отклонение: \t {df[i].std():.1f}')
        file.write(f'\nКоэффициент вариации: \t {round(coef_var, 2)}\n\n')