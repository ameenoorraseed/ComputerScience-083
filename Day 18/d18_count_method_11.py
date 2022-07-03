my_tuple = (88, 44, 155, 66, 1, 2, 3,66, 45, 66, 77, 66, 155, 66, 996)

# print(my_tuple.count(5))

count = 0
element = 155

for i in my_tuple:
	if i == element:
		count +=1

if count == 0:
	print("Element is not inside the tuple")
else:
	print("The count of",element,"is",count)