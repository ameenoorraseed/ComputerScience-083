
# alpha and digit
c = '#password123'
no_alpha = 0
no_digits = 0

for i in range(0,len(c)):
	if c[i].isalpha():
		no_alpha = no_alpha + 1

	elif c[i].isdigit():
		no_digits = no_digits + 1

print("the no of alphabets in", c , "is" , no_alpha)
print("the no of digits in", c , "is" , no_digits)