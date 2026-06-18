numbers = [1,2,3,45,56,]
print(numbers)
numbers.append(100)
print(numbers)
numbers.insert(1, 50)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print("список:",numbers)
print("первый элемент:",numbers[0])
print("последний элемент:",numbers[-1])





names = ["Ali","Zulii","Elbek","Tilek","Ramis","Nursultan"]

print(names[0:3])
print(names[4:6])
print(names.index("Ramis"))
names.remove("Tilek")
print(names)
names.append("Doni")
names.append("Sabyr")
print("Итоговый список:", names)




city_tuple = ("Naryn", "Osh", "Bishkek", "Batken","Talas")
print(city_tuple[0:3])
print(city_tuple[4:5])

city_list = list(city_tuple)
print(city_list)

city_list.append("Kara suu")
city_list.append("Chuy")
print(city_list)

city_list.remove("Osh")
print(city_list)

city_tuple = tuple(city_list)
print(city_tuple)





numbers = [5, 10, 15, 20, 25, 30]
print(numbers[0:3])
print(numbers[4:6])
numbers.append(35)
print(numbers)
numbers.remove(10)
print(numbers)
print(numbers.index(25))
print(len(numbers))