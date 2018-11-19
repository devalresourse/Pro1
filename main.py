Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'Olanewaju'
>>> s[3]
'n'
>>> students = ['Akin', 'Blont', 'Mikky', 'Pound']
>>> students[3]
'Pound'
>>> students.append['Wale']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    students.append['Wale']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> students.append('Wale')
>>> students
['Akin', 'Blont', 'Mikky', 'Pound', 'Wale']
>>> 
