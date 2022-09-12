def recognize (x, y , z):
	d = not(x or y or z) == (not x and not y and not z)
	print(d)


x = 1
y = 2
z = 'Я Егор'

recognize(x, y, z)