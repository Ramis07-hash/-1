
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")


with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)







name = input("Введите имя: ")


with open("names.txt", "a", encoding="utf-8") as file:
    file.write(name + "\n")


with open("names.txt", "r", encoding="utf-8") as file:
    print("Список имен:")
    print(file.read())