Set and Booleans
There are two other object types in Python that we should quickly cover. Sets and Booleans.

Sets
Sets are an unordered collection of unique elements. We can construct them by using the set() function. Let's go ahead and make a set to see how it works

In [1]:
x = set()
In [3]:
# We add to sets with the add() method
x.add(1)
In [4]:
#Show
x
Out[4]:
{1}

Note the curly brackets. This does not indicate a dictionary! Although you can draw analogies as a set being a dictionary with only keys.

We know that a set has only unique entries. So what happens when we try to add something that is already in a set?

In [5]:
# Add a different element
x.add(2)
In [6]:
#Show
x
Out[6]:
{1, 2}