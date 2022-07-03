# u_list = [ -43, 44, 45, 49, 56, 443, 889 ]

u_list = [ 12, 1.6, 10, -17, 8, 0.0025, 3 ]

size = len(u_list)

for first in range(size): 		# i 7
	for second in range(size):	# j 7
		
		if u_list[first] < u_list[second]:
			u_list[first],u_list[second] = u_list[second],u_list[first]
			print(u_list)
	




print(u_list)



