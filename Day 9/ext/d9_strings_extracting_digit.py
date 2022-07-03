# extracting numbers

input_string = '0pa#@$@#$wwss4w#ossr3elllsfgfg#s$2$ fgfgd~fgfs1fddsgfglobpk;lvbodosoirlgdfg~sfg0sdfg/sdgf' 	# unreadable

output_special = ""						# only digits 
output_alpha = ""		
for char in input_string:				# traversal

	if not char.isalnum():
		output_special = output_special+ char
	
	elif char.isalpha():
		output_alpha = output_alpha + char


print("the alphabets in", output_alpha, "is" , len(output_alpha))
print("\n\nthe special in", output_special , "is" , len(output_special))
