choice = input("Выберите способ конвертации:\n1. Из Цельсия в Фаренгейты\n2. Из Фаренгейтов в Цельсии\n Ваш выбор (1/2): ")

if choice == '1':
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} градусов Цельсия равны {fahrenheit} градусам Фаренгейта.")
elif choice == '2':
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} градусов Фаренгейта равны {celsius} градусам Цельсия.")
else:
    print("Неверный выбор. Пожалуйста, выберите 1 или 2.")