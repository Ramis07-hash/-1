People = ["Ariet","Dovud","Ramis","Zulii","Maksat"]
print(People)
People.append("Aibek")
print(People)
People.insert(1, "Akyl")
print(People)
People.remove("Maksat")
print(People)




name = "Programming"
print(name[0:5])
print(name[8:11])
print(name[::-1])




cities_tuple = ("Batken", "Bishkek", "Osh", "Naryn")
print(cities_tuple)
print(cities_tuple[1])
cities_list = list(cities_tuple)
print(cities_list)
cities_list.append("Talas")
print(cities_list)
cities_tuple = ("Batken", "Bishkek", "Osh", "Naryn","Talas")
print(cities_tuple)