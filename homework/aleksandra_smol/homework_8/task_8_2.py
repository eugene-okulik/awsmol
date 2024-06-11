import sys

sys.set_int_max_str_digits(100001)


def fibo_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


numbers = [5, 200, 1000, 100000]
num = numbers[0]
count = 1

for i in fibo_gen(100000):

    if count == num:
        print(f'{num} = {i}')

        numbers.pop(0)
        if len(numbers) > 0:
            num = numbers[0]
        else:
            break
    count += 1
