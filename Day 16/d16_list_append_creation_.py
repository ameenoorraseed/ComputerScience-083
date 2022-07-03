
# write a program to get no. of elements from the user and create a new list

my_list = [] 
no_of_element = int(input("Enter the no. of elements to be added: "))

for i in range(no_of_element):
	new_element = int(input("Enter the new element: "))
	my_list.append(new_element)

print(my_list)

