
Numbers and more in Python!
In this lecture, we will learn about numbers in Python and how to use them.

We'll learn about the following topics:

1.) Types of Numbers in Python
2.) Basic Arithmetic
3.) Differences between Python 2 vs 3 in division
4.) Object Assignment in Python


Types of numbers
Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and floating point numbers.

Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.

Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.

Throughout this course we will be mainly working with integers or simple float number types.

Here is a table of the two main types we will spend most of our time working with some examples:

Examples	Number "Type"
1,2,-5,1000	Integers
1.2,-0.5,2e2,3E2	Floating-point numbers

Now let's start with some basic arithmetic.

Basic Arithmetic
In [1]:
# Addition
2+1
Out[1]:
3
In [2]:
# Subtraction
2-1
Out[2]:
1
In [3]:
# Multiplication
2*2
Out[3]:
4
In [4]:
# Division
3/2
Out[4]:
1


Whoa! What just happened? Last time I checked, 3 divided by 2 is equal 1.5 not 1!

The reason we get this result is because we are using Python 2. In Python 2, the / symbol performs what is known as "classic" division, this means that the decimal points are truncated (cut off). In Python 3 however, a single / performs "true" division. So you would get 1.5 if you had inputed 3/2 in Python 3.

So what do we do if we are using Python 2 to avoid this?

There are two options:

Specify one of the numbers to be a float:

In [11]:
# Specifying one of the numbers as a float
3.0/2
Out[11]:
1.5
In [12]:
# Works for either number
3/2.0
Out[12]:
1.5
We could also "cast" the type using a function that basically turns integers into floats. This function, unsurprisingly, is called float().

In [14]:
# We can use this float() function to cast integers as floats:
float(3)/2
Out[14]:
1.5
We will go over functions in much more detail later on in this course, so don't worry if you are confused by the syntax here. Consider this a sneak preview.

