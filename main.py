import math

result = 0

print("Возможные действия: ")
print("0) Выход из программы ")
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

def actions():
    while (True):
        try:
            sign = int(input("Введите действие: "))
            if (sign == 0):
                print("Выход из программы")
                break
            num = float(input("Введите первое число: "))
            num1 = float(input("Введите второе число: "))
        except ValueError:
            print("Это не то что нужно!")

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
            if (num < 0 or num1 < 0):
                print('Нельзя отрицательное')
            elif(num > 0 or num1 > 0):
                result = math.sqrt(num), math.sqrt(num1)
                print(result)
        elif (sign == 7):
            if (num < 0 or num1 < 0):
                print('Нельзя отрицательное')
            elif(num > 0 or num1 > 0):
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

actions()
