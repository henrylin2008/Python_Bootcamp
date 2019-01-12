Comprehensions
In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.

List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets. For a simple example:

Example 1
In [1]:
# Grab every letter in string
lst = [x for x in 'word']
In [2]:
# Check
lst
Out[2]:
['w', 'o', 'r', 'd']
This is the basic idea of a list comprehension. If you're familiar with mathematical notation this format should feel familiar for example: x^2 : x in { 0,1,2...10}


Lets see a few more example of list comprehensions in Python:

Example 2
In [1]:
# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
In [2]:
lst
Out[2]:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


Example 3
Lets see how to add in if statements:

In [5]:
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
In [6]:
lst
Out[6]:
[0, 2, 4, 6, 8, 10]