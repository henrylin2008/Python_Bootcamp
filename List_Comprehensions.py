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