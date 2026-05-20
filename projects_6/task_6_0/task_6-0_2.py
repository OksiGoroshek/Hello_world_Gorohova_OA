import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in df.columns[2:]:
    with open('means_6-0_2.txt', 'a', encoding='utf-8') as file:
        file.write(i)
        file.write(': ')
        file.write(f'{round(df[i].mean(), 2)}\n')