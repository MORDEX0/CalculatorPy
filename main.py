import math

result = 0

print("Возможные действия: ")
print("1) Сложение ")
print("2) Вычитание ")
print("3) Умножение ")
print("4) Деление ")
print("5) Возведение в степень ")
print("6) Квадратный корень ")
print("7) Факториал ")
print("8) Синус ")
print("9) Косинус ")
print("10) Тангенс ")

while (True):
    sign = int(input("Введите действие: "))
    num = float(input("Введите первое число: "))
    num1 = float(input("Введите второе число: "))
    if (sign==1):
        result = num + num1
        print(result)
    elif (sign == 2):
        result = num - num1
        print(result)
    elif (sign == 3):
        result = num * num1
        print(result)
    elif (sign == 4):
        if (num1 != 0):
            result = num / num1
            print(result)
        elif (num1 == 0):
            print("На ноль делить нельзя")
    elif (sign == 5):
        result = num ** num1
        print(result)
    elif (sign == 6):
        result = math.sqrt(num), math.sqrt(num1)
        print(result)
    elif (sign == 7):
        result = math.factorial(int(num)), math.factorial(int(num1))
        print(result)
    elif (sign == 8):
        result = math.sin(num), math.sin(num1)
        print(result)
    elif (sign == 9):
        result = math.cos(num), math.cos(num1)
        print(result)
    elif (sign == 10):
        result = math.tan(num), math.tan(num1)
        print(result)
    elif (sign < 1, sign > 10):
        print("Такого действия нет!!!!")
        break




