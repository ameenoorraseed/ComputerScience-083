my_list = [4,5,6]

new_elements = [44,55,66]

# my_list.append(new_elements) 	# add in the last
my_list.extend(new_elements)    # populate or increase
								# extend will not create a nested list

print(len(my_list))
