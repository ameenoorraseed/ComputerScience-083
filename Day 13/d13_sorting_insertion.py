u_list = [ -43, 44, 45, 49, 56, 443, 889 ]
size = len(u_list)

for element in range(1,size):
	key = u_list[element]  # 44
	j = element-1 #index is 2-1 -> -43

	#Compare each left small +++key+++ right big
	while j>=0 and key < u_list[element]:  # [-43, 44, 45, 49, 56, 443, 889]  
		u_list[element+1] = u_list[element]
		j -=1

	u_list[element] = key

print("After sorting",u_list)




