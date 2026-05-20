import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in df.columns[1:]:
    with open('modes_6-0_4.txt', 'a', encoding='utf-8') as file:
        file.write(i)
        file.write(': ')
        file.write(f'{df[i].mode()}\n')