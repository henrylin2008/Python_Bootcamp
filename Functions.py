Functions
Introduction to Functions
This lecture will consist of explaining what a function is in Python and how to create one. Functions will be one of our main building blocks when we construct larger and larger amounts of code to solve problems.

So what is a function?

Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions.

On a more fundamental level, functions allow us to not have to repeatedly write the same code again and again. If you remember back to the lessons on strings and lists, remember that we used a function len() to get the length of a string. Since checking the length of a sequence is a common task you would want to write a function that can do this repeatedly at command.

Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).

Example 1: A simple print 'hello' function
In [4]:
def say_hello():
    print 'hello'
Call the function

In [5]:
say_hello()
hello

Example 2: A simple greeting function
Let's write a function that greets people with their name.

In [6]:
def greeting(name):
    print 'Hello %s' %name
In [7]:
greeting('Jose')
Hello Jose

Using return
Let's see some example that use a return statement. return allows a function to return a result that can then be stored as a variable, or used in whatever manner a user wants.

Example 3: Addition function
In [8]:
def add_num(num1,num2):
    return num1+num2
In [9]:
add_num(4,5)
Out[9]:
9
In [10]:
# Can also save as variable due to return
result = add_num(4,5)
In [11]:
print result
9