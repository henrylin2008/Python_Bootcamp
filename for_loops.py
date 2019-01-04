for Loops
A for loop acts as an iterator in Python, it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings,lists,tuples, and even built in iterables for dictionaries, such as the keys or values.

We've already seen the for statement a little bit in past lectures but now lets formalize our understanding.

Here's the general format for a for loop in Python:

for item in object:
    statements to do stuff


The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside you loop, for example if you wanted to use if statements to perform checks.

Let's go ahead and work through several example of for loops using a variety of data object types. we'll start simple and build more complexity later on.

Example 1
Iterating through a list.

In [1]:
# We'll learn how to automate this sort of list in the next lecture
l = [1,2,3,4,5,6,7,8,9,10]
In [2]:
for num in l:
    print num
1
2
3
4
5
6
7
8
9
10
Great! Hopefully this makes sense. Now lets add a if statement to check for even numbers. We'll first introduce a new concept here--the modulo.