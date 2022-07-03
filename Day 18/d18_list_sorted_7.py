
my_tuple = (88, 44, -55, 66)

# ascending 
new = sorted(my_tuple)
new = tuple(new)
print("old tuple", my_tuple,type(my_tuple))
print("new tuple", type(new))

# descending
new = tuple(sorted(my_tuple,reverse=True))
print("old tuple", type(my_tuple))
print("new tuple",type(new))

