import pandas as pd
df = pd.read_csv('wild_boars.csv')
gender_length_75 = df.groupby('gender')['length_cm'].quantile(0.75)
gender_length_25 = df.groupby('gender')['length_cm'].quantile(0.25)
iqr = gender_length_75 - gender_length_25
with open('iqr_6-0_6.txt', 'w', encoding='utf-8') as file:
    file.write(str(iqr))