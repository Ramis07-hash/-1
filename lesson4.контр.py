a = int(input("введите первое число: "))
b = int(input("введите второе число: "))

if a > b:
    print("Первое число больше")
elif b > a:
    print("Второе число больше")
else:
    print("Числа равны")


if a > 0 and b > 0:
    print("Оба числа положительные")



    


num = int(input("введите число: "))


if 1 <= num <= 10:
    print("Число в диапазоне 1–10")
elif num >= 11:
    print("Число в диапазоне 11–100")
else:
    print("Число вне диапазона")






name = input("введите имя: ")

length = len(name)

print("длина имени:", length)


if length < 5:
    print("Короткое имя")
elif 5 <= length <= 8:
    print("Среднее имя")
else:
    print("Длинное имя")





    

numbers = [7, 3, 15, 2]


print("Второй элемент:", numbers[1])


print("Последний элемент:", numbers[-1])

numbers[0], numbers[-1] = numbers[-1], numbers[0]


print("Обновлённый список:", numbers)






num2 = int(input("сумма покупки: "))
if num2 >=5000:
     print("скидка 10%")
elif num2 >=2000:
     print("скидка 5%")
else:  
     print("скидка нет") 




