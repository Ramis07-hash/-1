# Запись в файл
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

# Чтение файла
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read())









# Ввод имени
name = input("Введите имя: ")

# Добавление в файл
with open("names.txt", "a", encoding="utf-8") as file:
    file.write(name + "\n")

# Чтение файла
with open("names.txt", "r", encoding="utf-8") as file:
    print("Список имен:")
    print(file.read())