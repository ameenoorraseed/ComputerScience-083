
a = str(input("enter your mail id: "))#'sample@gmail.com'
if a[-10: ] == "@gmail.com":
	print('user is using gmail')

elif a[-10: ] == '@yahoo.com':
	print('user is using yahoo mail service')

else:
	print("user is using other mail service")




