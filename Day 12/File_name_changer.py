import os


os.chdir(r"L:\BBIC\Day 12")
s = os.getcwd()
for i in os.listdir(s): 
	os.rename(i,i.replace("d11", "d12"))
	print(i)