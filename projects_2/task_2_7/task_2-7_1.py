files = ["seq1", "seq2", "seq3", "seq4"]

for name in files:
    data = input('Введите дату взятия образца: ')
    new_name = name + '_' + data + ".fasta"
    print(f"{new_name}")