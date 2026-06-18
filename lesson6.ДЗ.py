student = {"name": "Ramis","age":19,"city":"Batken","grade":5}
print(student)
print(student["name"])
student["grade"]= 3
print(student)
student["email"]= "rmis@gmail.com"
print(student)





produkts = {"apple": 100, "banana": 80, "milk": 120, "bread": 60}
print(produkts)
print(produkts["banana"])
produkts.pop("bread")
print(produkts)
produkts["cheese"] = 300
print(produkts)

print(produkts.keys())
print(produkts.values())




numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.add(6)
print(numbers)
numbers.remove(2)
print(numbers)

print(len(numbers))
print(max(numbers))






set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1)
print(set2)

print(set1.union(set2))

print(set1.intersection(set2))

set1.add(10)
print(set1)







def sum_numbers():
    
    num1 = int(input("Биринчи санды киргиз: "))
    num2 = int(input("Экинчи санды киргиз: "))
    print(num1 + num2)
    
sum_numbers()
