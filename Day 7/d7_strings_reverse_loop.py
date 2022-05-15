a = "It is rainy now, and I feel so happy"
b = "sample"
size = len(a)
# for i in b: # traversal -> no index
# 	print(i)




# s a m p l e
#-6-5-4-3-2-1
# end value is not included +1 for pos -1 for negative
# for i in range(-1,-size-1,-1): #negative starts from -1
# 	print(b[i])

# for i in range(0,size,1):
# 	print(b[i])

# forward and reverse iteration in a same loop
# c = "one"
# o e
# n n
# e o

a = "It is rainy now, and I feel so happy"

forward_index = 0
for i in range(-1,-size-1,-1): #negative starts from -1
	print(a[forward_index],a[i])
	forward_index = forward_index + 1