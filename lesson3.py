# # есть два вида цикла
# # 1) for
# # 2)while


# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")


# for world in range(4):
#   print("hello world")

 
# for number in range(1, 11):
#   print(number)


# title = "Kyrgyzstan"
# n = 0
# for b in title:
#   n += 1
#   print(f"{n})  {b}")



# for i in range(5):
#    print("Я съел конфету ")

# holod = 5
# while holod > 0:
#    print("Съел конфету") 
#    holod -= 1
  


# while True:
#    print("Я люблю Python")




# n = 0
# while True:
#    n +=9
#    print(n)



# # int - Целые числа 
# # str - СТРОКА 
# # float - дробные числа 
# # bool -  логический тип данных 


# # list - список 
# # students = []

# my_list = [34, 5.6, "Hello", [1, 2, 3]]
# print(my_list)

# num1 = "Askar"
# num2 = "Aibek"
# num3 = "Tilek"
# num4 = "Nursultan"
# num5 = "Aibek"


# students = ["Askar","Aibek","Tilek","Nursultan","Aibek"]
# print(students)
# students.append("Ramis") # Добавляет элемент в конец спска 
# print(students)
# students.insert(3, "Dovud") # Добавляет элемент в опередленную позицию 
# print(students)
# students.remove("Askar")  # Удаляет элемент из списка только по названию элемента 
# print(students)
# students.pop(4) # Удаляет элемент из списка по индексу
# print(students)
# students.sort() # Сортирует список 
# print(students)
# students.reverse() # Переворачивает список
# print(students)
# # students.clear() #  Очищает список 
# print(students)
# print(students.index("Nursultan"))
# print(students)


# names = ["Ali","Zulii","Elbek","Tilek","Ramis","Nursultan"]

# print(names[0:3])
# print(names[4:6])
# print(names.index("Ramis"))
# names.remove("Tilek")
# print(names)
# names.append("Doni")
# names.append("Sabyr")
# print("Итоговый список:", names)

# list = [1,2,3,45,56,]
# print(list)
# list.append(100)
# print(list)
# list.insert(1, 50)
# print(list)
# list.pop(0)
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print("список:",list)
# print("первый элемент:",list[0])
# print("последний элемент:",list[-1])





# student = [1, "ramis",3, [ 2,3,4,]]
# print(student)


# #индекс - нумерация символов в строке (саписке). которая начинается с 0

# name = "Kyrgyzstan"
#       #0123456789
# print(name[0:6])


# title = "Balluball"
# print(title[1:5])
# print(title[4:10])




# students = ["Askhat", "Dastan", "Jum", "Aidana"]

# List - Список []
# Список изменяемый тип данных


# # # Tuple - Кортеж ()
# # # Кортеж не изменяемый тип данных

# city_tuple = ("Naryn", "Osh", "Bishkek", "Batken","Talas")
# print(city_tuple[0:3])
# print(city_tuple[4:5])
# city_list = list(city_tuple)
# print(city_list)
# city_list.append("Kara suu")
# city_list.append("Chuy")
# print(city_list)
# city_list.remove("Osh")
# print(city_list)
# city_tuple = tuple(city_list)
# print(city_tuple)


# People = ["Ariet","Dovud","Ramis","Zulii","Maksat"]
# print(People)
# People.append("Aibek")
# print(People)
# People.insert(1, "Akyl")
# print(People)
# People.remove("Maksat")
# print(People)




# name = "Programming"
# print(name[0:5])
# print(name[8:11])
# print(name[::-1])




# cities_tuple = ("Batken", "Bishkek", "Osh", "Naryn")
# print(cities_tuple)
# print(cities_tuple[1])
# cities_list = list(cities_tuple)
# print(cities_list)
# cities_list.append("Talas")
# print(cities_list)
# cities_tuple = ("Batken", "Bishkek", "Osh", "Naryn","Talas")
# print(cities_tuple)





# numbers = [5, 10, 15, 20, 25, 30]
# print(numbers[0:3])
# print(numbers[4:6])
# numbers.append(35)
# print(numbers)
# numbers.remove(10)
# print(numbers)
# print(numbers.index(25))
# print(len(numbers))