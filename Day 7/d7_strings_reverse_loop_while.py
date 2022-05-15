a = "It is rainy now, and I feel so happy"


# forward_index = 0

#size = len(b) # 6



# # len()
# .format

reverse_index = -1 #-6
# size = len(b)
# while reverse_index >= -size:   	# -6 > -6  #-1 -2 -3 -4
# 	print(b[reverse_index])
# 	reverse_index = reverse_index - 1

b = "sample"
reverse_index = -1
forward_index = 0
size = len(b) # 6
while forward_index < size: # 0<6
	print(b[forward_index], b[reverse_index]) # 0
	forward_index = forward_index + 1
	reverse_index = reverse_index - 1
	