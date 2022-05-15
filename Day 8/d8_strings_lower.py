a = '123PASSWORD'
b = 'kiwi fruit'
c = 'pasSWOrd123'
d = '$biN12'

print( a.lower() ) # converts all alphabets to lowercase
print( b.lower() )
print( c.lower() )
print( d.lower() )

# >>> b = 'kiwi fruit'                                                        
# >>> b                                                                       
# 'kiwi fruit'                                                                
# >>> b.capitalize()                                                          
# 'Kiwi fruit'                                                                
# >>> b.isdigit()                                                             
# False                                                                       
# >>> b.isspace()                                                             
# False                                                                       
# >>> b.isalnum()                                                             
# False                                                                       
# >>> 
# >>> b                                                                       
# 'kiwi fruit'                                                                
# >>> d = '$biN12'                                                            
# >>> d.islower()                                                             
# False                                                                       
# >>>                                                                         
# >>> d = '$bin12'                                                            
# >>> d.islower()                                                             
# True                                                                        
# >>> 