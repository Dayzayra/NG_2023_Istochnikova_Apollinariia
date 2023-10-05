import math
print("Доступные операции:\n 1. Сложение (+)\n 2. Вычитание (-)\n 3. Умножение (*)\n 4. Деление (/)\n 5. Извлечение корня (корень)\n 6. Возведение в степень (степень)")

choice = input("Выберите операцию (введите соответствующую цифру): ")

if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        result = num1 / num2
        operation = "/"
    elif choice == '5':
        result = math.sqrt(num1)
        operation = "корень"
    elif choice == '6':
        result = num1 ** num2
        operation = "степень"

    print(f"Результат: {num1} {operation} {num2} = {result}")
else:
    print("Неправильный выбор операции.")