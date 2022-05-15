# while loop
# break breaks the loop completely

# 1 4 7 10 
# 1 2 3 4
start = 1
end = 50
step = 3

while True:
	if start >= end:
		break
	print(start)
	start = start + step