Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
>>> 
>>> s = 'hello'
>>> 
>>> l[-1]
'f'
>>> 
>>> s[-1]
'o'
>>> l
['a', 'b', 'c', 'd', 'e', 'f']
>>> 
>>> l[-1]
'f'
>>> s[-1]
'o'
>>> # update -> modifying a new value
>>> 
>>> l[-1] = 1000
>>> l
['a', 'b', 'c', 'd', 'e', 1000]
>>> l[2] = 0
>>> 
>>> l
['a', 'b', 0, 'd', 'e', 1000]
>>> l[-1]=0
>>> 
>>> l
['a', 'b', 0, 'd', 'e', 0]
>>> 
>>> # list is changeable
>>> # mutable
>>> 
>>> s
'hello'
>>> 
>>> s[-1]
'o'
>>> s[-1] = 1000
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[-1] = 1000
TypeError: 'str' object does not support item assignment
>>> 
>>> s[0]
'h'
>>> 
>>> s[0] = 'm'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s[0] = 'm'
TypeError: 'str' object does not support item assignment
>>> 
>>> # str is immutable
>>> # list is mutable
>>> l
['a', 'b', 0, 'd', 'e', 0]
>>> l[0]
'a'
>>> 
>>> l[0] = 'sample'
>>> 
>>> l
['sample', 'b', 0, 'd', 'e', 0]
>>> l[0] = 's'
>>> l
['s', 'b', 0, 'd', 'e', 0]
>>> 
>>> 
>>> a = []
>>> b = 'hello'
>>> c = 'orange'
>>> 
>>> a = [b,c]
>>> a
['hello', 'orange']
>>> 
>>> a
['hello', 'orange']
>>> 
>>> a[-1]
'orange'
>>> 
>>> a[-2]
'hello'
>>> a[-2] = 100
>>> 
>>> a
[100, 'orange']
>>> 
>>> # deleting the list element and whole list
>>> 
>>> l
['s', 'b', 0, 'd', 'e', 0]
>>> 
>>> len(l)
6
>>> # len(l) -> counts from 1
>>> l[6]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l[6]
IndexError: list index out of range
>>> 
>>> 
>>> l
['s', 'b', 0, 'd', 'e', 0]
>>> 
>>> [4]
[4]
>>> l
['s', 'b', 0, 'd', 'e', 0]
>>> l
['s', 'b', 0, 'd', 'e', 0]

>>> 
>>> 
>>> 
>>> 
>>> l
['s', 'b', 0, 'd', 'e', 0]
>>> 
>>> l[4]
'e'
>>> 
>>> l[-3]
'd'
>>> 
>>> del l[-3]
>>> 
>>> len(l)
5
>>> 
>>> l
['s', 'b', 0, 'e', 0]
>>> 
>>> del l[1]
>>> 
>>> l
['s', 0, 'e', 0]
>>> 
>>> len(l)
4
>>> 
>>> 
>>> l
['s', 0, 'e', 0]
>>> 
>>> # deleting the whole list
>>> 
>>> l
['s', 0, 'e', 0]
>>> 
>>> del l
>>> 
>>> l
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> 
>>> 
>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
>>> 
>>> del l[1:4]
>>> l
['a', 'e', 'f']
>>> 
>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del l[-2:]
>>> l
['a', 'b', 'c', 'd']
>>> 
>>> 