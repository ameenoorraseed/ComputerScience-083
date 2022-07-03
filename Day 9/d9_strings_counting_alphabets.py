# counting no alphabets

s = '0pass4wor3#$$ d~~/'

# traversal
# iteration for or while

no_alphabets = 0
for i in s:
	if i.isalpha():
		no_alphabets = no_alphabets + 1

print("the no of alphabets in", s , "is" , no_alphabets)
