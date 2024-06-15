def my_calc_decor(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


@my_calc_decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))

print(calc(first_num, second_num))
