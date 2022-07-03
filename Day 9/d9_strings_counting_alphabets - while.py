# counting no alphabets

s = '0pass4wor3#$$ d~~/'

no_alphabets = 0
start = 0
stop = len(s)

while start < stop:
	if s[start].isalpha():
		no_alphabets = no_alphabets + 1
	start = start + 1


print("the no of alphabets in", s , "is" , no_alphabets)
