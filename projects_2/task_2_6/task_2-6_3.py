donor_phenotype = input('Введите фенотип группы крови донора(I, II, III, IV): ').strip().upper()
patient_phenotype = input('Введите фенотип группы крови пациента(I, II, III, IV): ').strip().upper()
if (donor_phenotype != 'I' and donor_phenotype != 'II' and donor_phenotype != 'III' and donor_phenotype != 'IV') \
or (patient_phenotype != 'I' and patient_phenotype != 'II' and patient_phenotype != 'III' and patient_phenotype != 'IV'):
    print('Группа крови не определена')
elif donor_phenotype == patient_phenotype or donor_phenotype == 'I':
    print('Переливание крови возможно')
else:
    print('Группа крови донора не подходит для переливания')