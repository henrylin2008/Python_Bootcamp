Lists
Earlier when discussing strings we introduced the concept of a sequence in Python. Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!

In this section we will learn about:

1.) Creating lists
2.) Indexing and Slicing Lists
3.) Basic List Methods
4.) Nesting Lists
5.) Introduction to List Comprehensions

Lists are constructed with brackets [] and commas separating every element in the list.

Let's go ahead and see how we can construct lists!

In [2]:
# Assign a list to an variable named my_list
my_list = [1,2,3]
We just created a list of integers, but lists can actually hold different object types. For example:

In [4]:
my_list = ['A string',23,100.232,'o']
Just like strings, the len() function will tell you how many items are in the sequence of the list.

In [6]:
len(my_list)
Out[6]:
4

Indexing and Slicing
Indexing and slicing works just like in strings. Let's make a new list to remind ourselves of how this works:

In [7]:
my_list = ['one','two','three',4,5]
In [10]:
# Grab element at index 0
my_list[0]
Out[10]:
'one'
In [11]:
# Grab index 1 and everything past it
my_list[1:]
Out[11]:
['two', 'three', 4, 5]
In [13]:
# Grab everything UP TO index 3
my_list[:3]
Out[13]:
['one', 'two', 'three']


We can also use + to concatenate lists, just like we did for strings.

In [14]:
my_list + ['new item']
Out[14]:
['one', 'two', 'three', 4, 5, 'new item']
Note: This doesn't actually change the original list!

In [15]:
my_list
Out[15]:
['one', 'two', 'three', 4, 5]
You would have to reassign the list to make the change permanent.

In [16]:
# Reassign
my_list = my_list + ['add new item permanently']
In [18]:
my_list
Out[18]:
['one', 'two', 'three', 4, 5, 'add new item permanently']
