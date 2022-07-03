# opening text file

file_1 = open("L:\\BBIC\\Day 22\\sample.txt","r")  # raw string - no translation -> escape seq
file_2 = open(r'L:\BBIC\Day 22\sample.txt') 
file_3 = open('sample.txt')

# read
data = file_1.read()

# close
file_1.close()