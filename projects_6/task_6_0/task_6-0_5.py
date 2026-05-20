import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in df.columns[2:]:
    with open('quantiles_6-0_5.txt', 'a', encoding='utf-8') as file:
        file.write(i)
        file.write(f'\n Перцентиль 25 (Q1): \t {df[i].quantile(0.25):.1f}')
        file.write(f'\n Медиана 50 (Q2): \t {df[i].quantile(0.5):.1f}')
        file.write(f'\n Перцентиль 75 (Q3): \t {df[i].quantile(0.75):.1f}')
        file.write(f'\n Перцентиль 33: \t {df[i].quantile(0.33):.1f}')
        file.write(f'\n Перцентиль 66: \t {df[i].quantile(0.66):.1f}')
        file.write(f'\n Максимальное: \t {df[i].quantile(1.00):.1f}\n\n')