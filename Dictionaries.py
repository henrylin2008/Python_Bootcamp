Dictionaries
We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.

This section will serve as a brief introduction to dictionaries and consist of:

1.) Constructing a Dictionary
2.) Accessing objects from a dictionary
3.) Nesting Dictionaries
4.) Basic Dictionary Methods
So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.


Constructing a Dictionary
Let's see how we can construct dictionaries to get a better understanding of how they work!

In [1]:
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
In [2]:
# Call values by their key
my_dict['key2']
Out[2]:
'value2'

Its important to note that dictionaries are very flexible in the data types they can hold. For example:

In [13]:
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
In [4]:
#Lets call items from the dictionary
my_dict['key3']
Out[4]:
['item0', 'item1', 'item2']
In [5]:
# Can call an index on that value
my_dict['key3'][0]
Out[5]:
'item0'
In [7]:
#Can then even call methods on that value
my_dict['key3'][0].upper()
Out[7]:
'ITEM0'