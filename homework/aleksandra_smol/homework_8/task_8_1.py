import random


def your_money(salary, bonus):
    if bonus:
        your_bonus = random.randrange(1, 10000)
        new_salary = salary + your_bonus
        return new_salary
    else:
        return salary


salary = int(input("Введите число: "))
bonus = random.randrange(1, 10000)

print(f"${your_money(salary, True)}")
print(f"${your_money(salary, False)}")
