import pandas as pd
df = pd.read_csv('wild_boars.csv')
for i in df.columns[2:]:
    with open('medians_6-0_3.txt', 'a', encoding='utf-8') as file:
        file.write(i)
        file.write(': ')
        file.write(f'{df[i].median():.2f}\n')