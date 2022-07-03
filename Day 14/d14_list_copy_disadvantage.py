Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> s = "sample"
>>> type(s)
<class 'str'>
>>> 
>>> l = [0,1,2,3,4]
>>> l
[0, 1, 2, 3, 4]
>>> 
>>> type(l)
<class 'list'>
>>> 
>>> s
'sample'
>>> 
>>> l
[0, 1, 2, 3, 4]
>>> 
>>> s[-1]
'e'
>>> s[-1] = '@@@@@@'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[-1] = '@@@@@@'
TypeError: 'str' object does not support item assignment
>>> 
>>> l
[0, 1, 2, 3, 4]
>>> 
>>> l[-1]
4
>>> l[-1] = 'new value'
>>> l
[0, 1, 2, 3, 'new value']
>>> l[-1]
'new value'
>>> 
>>> 
>>> l[-1] = 0
>>> 
>>> l
[0, 1, 2, 3, 0]
>>> 
>>> 
>>> s
'sample'
>>> 
>>> t = s
>>> 
>>> t
'sample'
>>> 
>>> s
'sample'
>>> 
>>> t[-1] = 'okay'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t[-1] = 'okay'
TypeError: 'str' object does not support item assignment
>>> 
>>> p = q = t
>>> p
'sample'
>>> 
>>> q
'sample'
>>> 
>>> t
'sample'
>>> 
>>> q[-1] = 234
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    q[-1] = 234
TypeError: 'str' object does not support item assignment
>>> 
>>> l
[0, 1, 2, 3, 0]
>>> 
>>> 
>>> l = [1,2,3]
>>> 
>>> l
[1, 2, 3]
>>> 
>>> m = l
>>> 
>>> 
>>> m
[1, 2, 3]
>>> 
>>> l
[1, 2, 3]

>>> 
>>> type(m)
<class 'list'>
>>> 
>>> type(l)
<class 'list'>
>>> 
>>> m[-1]
3
>>> 
>>> l[-1]
3
>>> 
>>> m
[1, 2, 3]
>>> 
>>> l
[1, 2, 3]
>>> 
>>> m[-1] = 100
>>> 
>>> m
[1, 2, 100]
>>> 
>>> l
[1, 2, 100]
>>> 
>>> 
>>> 
>>> n = m = l
>>> 
>>> n[0] = 8
>>> 
>>> m
[8, 2, 100]
>>> 
>>> n
[8, 2, 100]
>>> 
>>> l
[8, 2, 100]
>>> 
>>> del m[1]
>>> 
>>> m
[8, 100]
>>> 
>>> n
[8, 100]
>>> 
>>> l
[8, 100]
>>> 
>>> 