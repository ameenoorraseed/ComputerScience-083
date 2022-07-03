# counting alpha,digits and special characters
s = '0pas$%s4wor3#'

no_special_char = 0
no_alpha = 0
no_digit = 0

start = 0
end = len(s)

while start<end:
	if not s[start].isalnum():
		no_special_char = no_special_char + 1
	elif s[start].isalpha():
		no_alpha = no_alpha + 1
	elif s[start].isdigit():
		no_digit = no_digit +1
	start = start + 1

print('The no of special character in',s,"is",no_special_char)
print('The no of alpha in',s,"is",no_alpha)
print('The no of digits in',s,"is",no_digit)


