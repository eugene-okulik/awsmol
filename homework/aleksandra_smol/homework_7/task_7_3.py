resultat_1 = 'результат операции: 42'
resultat_2 = 'результат операции: 514'
resultat_3 = 'результат работы программы: 9'
resultat_4 = 'результат: 2'


def get_numbers(resultat):
    numb = int(resultat.split(":")[1])
    return numb + 10


print(get_numbers(resultat_1), get_numbers(resultat_2), get_numbers(resultat_3), get_numbers(resultat_4), sep="\n")
