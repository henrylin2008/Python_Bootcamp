range()
In this short lecture we will be discussing the range function. We haven't developed a very deep level of knowledge of functions yet, but we can understand the basics of this simple (but extremely useful!) function.

range() allows us to create a list of numbers ranging from a starting point up to an ending point. We can also specify step size. Lets walk through a few examples:

In [7]:
range(0,10)
Out[7]:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
In [8]:
x =range(0,10)
type(x)
Out[8]:
list

In [3]:
start = 0 #Default
stop = 20 
x = range(start,stop)
In [4]:
x
Out[4]:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Great! Notice how it went up to 20, but doesn't actually produce 20. Just like in indexing. What about step size? We can specify that as a third argument:

In [5]:
x = range(start,stop,2)
#Show
x
Out[5]:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Awesome! Well thats it...or is it?