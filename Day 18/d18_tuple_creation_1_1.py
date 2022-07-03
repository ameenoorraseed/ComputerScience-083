a = ()

for i in range(5):
	new_element = int(input("Enter the new element"))
	a = a + (new_element,)  # TypeError: can only concatenate tuple (not "int") to tuple

print(a)
