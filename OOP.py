Object Oriented Programming
Object Oriented Programming (OOP) tends to be one of the major obstacles for beginners when they are first starting to learn Python.

There are many,many tutorials and lessons covering OOP so feel free to Google search other lessons, and I have also put some links to other useful tutorials online at the bottom of this Notebook.

For this lesson we will construct our knowledge of OOP in Python by building on the following topics:

Objects
Using the class keyword
Creating class attributes
Creating methods in a class
Learning about Inheritance
Learning about Special Methods for classes
Lets start the lesson by remembering about the Basic Python Objects. For example:

In [1]:
l = [1,2,3]
Remember how we could call methods on a list?

In [3]:
l.count(2)
Out[3]:
1

What we will basically be doing in this lecture is exploring how we could create an Object type like a list. We've already learned about how to create functions. So lets explore Objects in general:

Objects
In Python, everything is an object. Remember from previous lectures we can use type() to check the type of object something is:

In [4]:
print type(1)
print type([])
print type(())
print type({})
<type 'int'>
<type 'list'>
<type 'tuple'>
<type 'dict'>
So we know all these things are objects, so how can we create our own Object types? That is where the class keyword comes in.

class
The user defined objects are created using the class keyword. The class is a blueprint that defines a nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. For example, above we created the object 'l' which was an instance of a list object.

Let see how we can use class: