day = int(input('Введите число: '))
if (day < 1 or day > 7):
	print('Ну ты вообще! Таких дней недели не бывает')
elif (day >= 1 and day <= 5):
	print('Это РАБОЧИЙ ДЕНЬ, СЫНОК')
else: 
	print('УРА Выходной!!!')