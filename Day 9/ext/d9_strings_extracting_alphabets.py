# counting no alphabets

input_string = '0pass4w#or3#$$ d~~/' 	# unreadable

output_string = ""						# only alpha - password

for char in input_string:				# traversal

	if char.isalpha():
		output_string = output_string + char

print("the alphabets in", input_string , "is" , output_string)
