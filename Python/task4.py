numTerm = int(input("Введите номер четверти: "))
if(numTerm == 1):
	print("Диапазон возможных значений \nX:(0,+inf)\nY:(0,+inf)")
elif(numTerm == 2):
	print("Диапазон возможных значений \nX:(-inf,0)\nY:(0,+inf)")
elif(numTerm == 3):
	print("Диапазон возможных значений \nX:(-inf,0)\nY:(-inf,0)")
elif(numTerm == 4):
	print("Диапазон возможных значений \nX:(0,+inf)\nY:(-inf,0)")
else:
	print('Такой четверти не существует, она поэтому так и называется ЧЕТВЕРТЬ')


