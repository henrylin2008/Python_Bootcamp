Decorators
Decorators can be thought of as functions which modify the functionality of another function. They help to make your code shorter and more "Pythonic".

To properly explain decorators we will slowly build up from functions. Make sure to restart the Python and the Notebooks for this lecture to look the same on your own computer. So lets break down the steps:

Functions Review
In [1]:
def func():
    return 1
In [2]:
func()
Out[2]:
1

Scope Review
Remember from the nested statements lecture that Python uses Scope to know what a label is referring to. For example:

In [6]:
s = 'Global Variable'

def func():
    print locals()
Remember that Python functions create a new scope, meaning the function has its own namespace to find variable names when they are mentioned within the function. We can check for local variables and global variables with the local() and globals() functions. For example: