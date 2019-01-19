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