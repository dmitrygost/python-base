

while True:
    num = int(input("Введите число: "))
    sum = 0
    if num == 0:
        print("Цикл завершен")
        break
    while num != 0:
        num1 = num % 10
        num = num // 10
        sum += num1
    print("Сумма цифр числа равна:", sum)










































