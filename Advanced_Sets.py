In this lecture we will learn about the various methods for sets that you may not have seen yet. We'll go over the basic ones you already know and then dive a little deeper.

In [2]:
s = set()
add
add elements to a set. Remember a set won't take duplicate elements and only present them once (thats why its called a set!)

In [3]:
s.add(1)
In [4]:
s.add(2)
In [5]:
s
Out[5]:
{1, 2}

clear
removes all elements from the set

In [6]:
s.clear()
In [7]:
s
Out[7]:
set()

copy
returns a copy of the set. Note it is a copy, so changes to the original don't effect the copy.

In [10]:
s = {1,2,3}
sc = s.copy()
In [11]:
sc
Out[11]:
{1, 2, 3}
In [12]:
s
Out[12]:
{1, 2, 3}
In [13]:
s.add(4)
In [14]:
s
Out[14]:
{1, 2, 3, 4}
In [15]:
sc
Out[15]:
{1, 2, 3}


difference
difference returns the difference of two or more sets. The syntax is:

set1.difference(set2)
For example:

In [17]:
s.difference(sc)
Out[17]:
{4}