import pandas as pd
df = pd.read_csv('wild_boars.csv')
tusk_s = df.groupby('gender')['tusk_length_cm'].std()
tusk_m = df.groupby('gender')['tusk_length_cm'].mean()
coef_var = (tusk_s / tusk_m) * 100
with open('coef_var_6-0_8.txt', 'w', encoding='utf-8') as file:
    file.write(str(round(coef_var, 2)))