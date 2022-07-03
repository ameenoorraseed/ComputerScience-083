
# counting special characters
s = '0pass4wor3#'

no_special_char = 0
start = 0
end = len(s)

while start<end:
	if not s[start].isalnum():
		no_special_char = no_special_char + 1
	start = start + 1

print('The no of special character in',s,"is",no_special_char)


