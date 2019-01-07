In this section of the course we will be learning about the difference between iteration and generation in Python and how to construct our own Generators with the yield statement. Generators allow us to generate as we go along, instead of holding everything in memory.

We've touch on this topic in the past when discussing the range() function in Python 2 and the similar xrange(), with the difference being the xrange() was a generator.

Lets explore a little deeper. We've learned how to create functions with def and the return statement. Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. This type of function is a generator in Python, allowing us to generate a sequence of values over time. The main difference in syntax will be the use of a yield statement.

In most aspects, a generator function will appear very similar to a normal function. The main difference is when a generator function is compiled they become an object that support an iteration protocol. That means when they are called in your code the don't actually return a value and then exit, the generator functions will automatically suspend and resume their execution and state around the last point of value generation. The main advantage here is that instead of having to compute an entire series of values upfront and the generator functions can be suspended, this feature is known as state suspension.

￼￼To start getting a better understanding of generators, lets go ahead and see how we can create some.

In [6]:
# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3
In [10]:
for x in gencubes(10):
    print x
0
1
8
27
64
125
216
343
512
729
Great! Now since we have a generator function we don't have to keep track of every single cube we created.

Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time.

As we've noted in previous lectures (such as range()) many Standard Library functions that return lists in Python 2 have been modified to return generators in Python 3 because generators.