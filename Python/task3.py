x = int(input("Введите переменную X: "))
y = int(input("Введите переменную Y: "))

if (x > 0 and y > 0):
	print("Вы попали в плоскость 1")
elif (x < 0 and y > 0):
	print("Вы попали в плоскость 2")
elif (x < 0 and y < 0):
	print("Вы попали в плоскость 3")
elif (x > 0 and y < 0):
	print("Вы попали в плоскость 4")
elif (x == 0 and y != 0):
	print("Вы попали на ось ординат")
elif (x != 0 and y == 0):
	print("Вы попали на ось абсцис")
else:
	print("Не соостветствует условию задачи")



	

	


