# tuple comprehension -> generator
# write a program to get no. of elements from the user and create a new tuple

#print([int(input("Enter the new element: ")) for i in range(int(input("Enter the no. of elements to be added: "))) ])


b = (i for i in range(12))
print(next(b))
print(next(b))
print(next(b))

