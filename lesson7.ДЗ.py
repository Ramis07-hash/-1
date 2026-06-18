def check_number():
    num = int(input("Введите число: "))
    
    if num % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")


check_number()
check_number()
check_number()






def calculate(a, b):
    print("Сумма:", a + b)
    print("Произведение:", a * b)


calculate(5, 10)
calculate(7, 3)








subtract = lambda a, b: a - b
print(subtract(10, 3))






numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


multiplied_numbers = list(map(lambda x: x * 3, numbers))

print("Четные числа:", even_numbers)
print("Числа умноженные на 3:", multiplied_numbers)