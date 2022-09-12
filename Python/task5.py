from cmath import sqrt


x = int(input("Введите переменную X: "))
y = int(input("Введите переменную Y: "))

x1 = int(input("Введите переменную X1: "))
y1 = int(input("Введите переменную Y1: "))

print(sqrt((x-x1)**2 + (y-y1)**2).real)
