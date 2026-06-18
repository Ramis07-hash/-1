for num in range(1, 21):
    print(num)





for i in range(1, 11):
    print(f"5 * {i} = {5 * i}")




numbers = [2, 4, 6, 8, 10]

for i in numbers:
    print(i *3)





try:
    num = int(input("Ввведите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(num / num2)
except ValueError:
    print("Введите  число")
except ZeroDivisionError:
    print("На ноль делить нельзя")    
