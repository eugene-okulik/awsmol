numb = 37

while True:
    personal_input = int(input("Введите цифру:"))
    if personal_input == numb:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова!")
