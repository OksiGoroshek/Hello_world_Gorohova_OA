import pandas as pd
df = pd.read_csv('wild_boars.csv')
print(f'Столбец содержащий длину клыков:\n{df['tusk_length_cm']}')
print(f'Самые длинные клыки(см): {df['tusk_length_cm'].max()}')
print(f'Самые короткие: {df['tusk_length_cm'].min()}')