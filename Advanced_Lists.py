In this series of lectures we will be diving a little deeper into all the methods available in a list object. These aren't officially "advanced" features, just methods that you wouldn't typically encounter without some additional exploring. Its pretty likely that you've already encountered some of these yourself!

Lets begin!

In [1]:
l = [1,2,3]
append
You will have definitely have use this method by now, which merely appends an element to the end of a list:

In [2]:
l.append(4)

l
Out[2]:
[1, 2, 3, 4]



count
We discussed this during the methods lectures, but here it is again. count() takes in an element and returns the number of times it occures in your list:

In [4]:
l.count(10)
Out[4]:
0
In [5]:
l.count(2)
Out[5]:
1
