
# # int - Целые числа 
# # str - СТРОКА 
# # float - дробные числа 
# # bool -  логический тип данных 


# # list - список - 
# # tuple - кортеж



# # dict -словарь изменяемый {} -
# # set -множество -изменяемый
# # frozenset -неизменяемое множество/

# # dictinary dict -Словрь- не работает индексы

# # # key -ключ
# # # value -значение
# # items- элементы

# # ключ - всегда указывается в начале (перед значением),всегда уникальный всегда указывается в кавычках
# # значение -Всегда указывается после ключа (:) может быть любым типом данных,может быть любым количеством можно не уникальный 

# student = {"name": "Nurbolot", "age": 20}


# test = {"car": "BMW", "model": "X5", "year": 2022, "color": "black", "style":"style"}
# print(test)
# print(test['model'])
# print(test['color'])
# test.pop("style")
# print(test)
# test ["price"]= "50.000$"
# print(test)



# test ["year"] = 2024
# print(test)

# print(test.keys())
# print(test.values())
# print(test.items())




# # set set множество Изменяемый {} Не имеет дубликатов Не имеет порядка


# students = {"Nurbolot", "Askar", "Aktan", "Nurbolot"}
# print(students)
# students.add("Islam")
# print(students)
# students.remove("Askar")
# print(students)




 
# test = {1,1.0,"1", True}
# print(test)


# test = frozenset ([1,2,3,4,5,6])
# print(test)

# test2 = {7,8,9,10,11}
# print(test2)

# # Функция

# # 1) Встроенные функции
# # 2) Пользовательские функции
# # 3) Анонимные функции




# def name():
#     print("Hello")

# name()
# name()


# # Создайте пустой словарь products.
# # Добавьте в этот словарь в ручную товары:
# # "apple": 10
# # "banana": 20
# # "orange": 30
# # Вывести цену мандарина (orange)
# # Добавить новый товар milk со значением 80
# # Вывести весь словарь


# produkts = {"apple": 10,"banana": 20,"orange": 30}
# print(produkts)
# print(produkts["orange"])
# produkts["milk"]= 80
# print(produkts)
# print(produkts)
 


# def name3():
#     number = int(input("введите число: "))
#     if number % 2 ==0:
#         print("четное")
#     else:
#         print("не четное")

# name3()


