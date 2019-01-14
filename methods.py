Methods
We've already seen a few example of methods when learning about Object and Data Structure Types in Python. Methods are essentially functions built into objects. Later on in the course we will learn about how to create our own objects and methods using Object Oriented Programming (OOP) and classes.

Methods will perform specific actions on the object and can also take arguments, just like a function. This lecture will serve as just a brief introduction to methods and get you thinking about overall design methods that we will touch back upon when we reach OOP in the course.

Methods are in the form:

object.method(arg1,arg2,etc...)


Lets take a quick look at what an example of the various methods a list has:

In [2]:
# Create a simple list
l = [1,2,3,4,5]
Fortunately, with iPython and the Jupyter Notebook we can quickly see all the possible methods using the tab key. The methods for a list are:

append
count
extend
insert
pop
remove
reverse
sort
Let's try out a few of them:

append() allows us to add elements to the end of a list:

In [3]:
l.append(6)
In [4]:
l
Out[4]:
[1, 2, 3, 4, 5, 6]