dna = input('Введите последовательность ДНК: ')
DNA = dna.upper()

print(f'\n=== Анализ последовательности ДНК ===\n\nПоследовательность ДНК: {DNA}\n\n')
print(f'Подсчет нуклеотидов:\nA: {DNA.count('A')}\nT: {DNA.count('T')}\nG: {DNA.count('G')}\nC: {DNA.count('C')}\n\n')
print(f'Общая длина: {len(DNA)}\n\n')
print(f'Процентное содержание:\nA: {round(DNA.count('A')/len(DNA), 2)*100}%\nT: {round(DNA.count('T')/len(DNA), 2)*100}%\nG: {round(DNA.count('G')/len(DNA), 2)*100}%\nC: {round(DNA.count('C')/len(DNA), 2)*100}%')