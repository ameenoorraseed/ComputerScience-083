
# counting no digits

c = 'password'


no_of_digits = 0

# first way - Traversal

for i in c:
	if i.isdigit():
		no_of_digits = no_of_digits + 1
print("the no of digits in", c , "is" , no_of_digits)


