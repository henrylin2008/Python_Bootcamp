An interesting feature of Python is the ability to chain multiple comparisons to perform a more complex test. You can use these chained comparisons as a shorthand for larger Boolean Expressions.

In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in python: and and or.

Let's look at a few examples of using chains:

In [1]:
1 < 2 < 3
Out[1]:
True

The above statement check if 1 was less than 2 and if 2 was less than 3. We could have written this using an and statement in Python:

In [2]:
1<2 and 2<3
Out[2]:
True

The and is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:

In [3]:
1 < 3 > 2
Out[3]:
True