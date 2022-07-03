# counting no digits

c = '0pass4wor3d'
start = 0
stop = len(c)
no_of_digits = 0

# third way - Iteration - while loop

while start < stop : # 0 < 7
	if c[start].isdigit():
		no_of_digits = no_of_digits + 1

	start = start + 1

print("the no of digits in", c , "is" , no_of_digits)


