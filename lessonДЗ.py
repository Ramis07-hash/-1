password = input("Введите пароль: ")

if password == "1234567890":
    print("Доступ разрешён")
else:
    print("Неверный пароль")



tariff = input("Введите название тарифа: ")

if tariff == "basic":
    print("Доступ к базовым функциям")
elif tariff == "standard":
    print("Доступ к стандартным функциям")
elif tariff == "premium":
    print("Полный доступ")
else:
    print("Тариф не найден")



temperature = int(input("Введите температуру: "))

if temperature > 30:
    print("Очень жарко")
elif 15 <= temperature <= 30:
    print("Тепло")
elif 5 <= temperature <= 14:
    print("Прохладно")
else:
    print("Холодно")




result = input("Введите результат экзамена (сдал / не сдал): ")

if result == "сдал":
    print("Поздравляем, экзамен сдан")
elif result == "не сдал":
    print("Экзамен не сдан")
else:
    print("Некорректный ввод")




text = input("Введите строку: ")

# первые 3 символа
print(text[:3])

# последние 3 символа
print(text[-3:])

# строка без первого и последнего символа
print(text[1:-1])

