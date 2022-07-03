# counting no digits

c = '0pass4wor3d'

no_of_digits = 0

# Second way - Iteration

for i in range(len(c)):
	if c[i].isdigit():
		no_of_digits = no_of_digits + 1

print("the no of digits in", c , "is" , no_of_digits)


