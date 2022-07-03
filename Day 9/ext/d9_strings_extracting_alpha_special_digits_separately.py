# extracting numbers

input_string = '0pa#@$@#$wwss4w#ossr3elllsfgfg#s$2$ fgfgd~fgfs1fddsgfglobpk;lvbodosoirlgdfg~sfg0sdfg/sdgf' 	# unreadable

output_string = ""						# only digits 

for char in input_string:				# traversal

	if not char.isalnum():
		output_string = output_string + char

print("the alphabets in", input_string , "is" , output_string)
