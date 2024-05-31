resultat_1 = 'результат операции: 42'
resultat_2 = 'результат операции: 514'
resultat_3 = 'результат работы программы: 9'

num_1 = resultat_1[resultat_1.index(':') + 2:]
num_2 = resultat_2[resultat_2.index(':') + 2:]
num_3 = resultat_3[resultat_3.index(':') + 2:]

total_1 = int(num_1) + 10
total_2 = int(num_2) + 10
total_3 = int(num_3) + 10

print(total_1, total_2, total_3, sep='\n')
