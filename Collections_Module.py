The collections module is a built-in module that implements specialized container data types providing alternatives to Python’s general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.

Now we'll learn about the alternatives that the collections module provides.

Counter
Counter is a dict subclass which helps count hash-able objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

Lets see how it can be used:

In [1]:
from collections import Counter
Counter() with lists

In [2]:
l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

Counter(l)
Out[2]:
Counter({1: 6, 2: 6, 3: 4, 32: 1, 12: 1, 21: 1, 223: 1})