String objects have a variety of methods we can use to save time and add functionality. Lets explore some of them in this lecture:

In [75]:
s = 'hello world'


Changing case
We can use methods to capitalize the first word of a string, change cases to upper and lower case strings.

In [76]:
# Capitalize first word in string
s.capitalize()
Out[76]:
'Hello world'
In [77]:
s.upper()
Out[77]:
'HELLO WORLD'
In [78]:
s.lower()
Out[78]:
'hello world'



Location and Counting
In [80]:
s.count('o')
Out[80]:
2
In [81]:
s.find('o')
Out[81]:
4
