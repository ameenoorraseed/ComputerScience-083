# how to update the tuple

t = (4,5,6,7)
l = list(t)
l[0] = 34		# so tuples are also not possbile to update because it is immutable
t = tuple(l)
del l
print(t,type(t))