Nested Statements and Scope
Now that we have gone over on writing our own functions, its important to understand how Python deals with the variable names you assign. When you create a variable name in Python the name is stored in a name-space. Variable names also have a scope, the scope determines the visibility of that variable name to other parts of your code.

Lets start with a quick thought experiment, imagine the following code:

In [6]:
x = 25

def printer():
    x = 50
    return x

print x
print printer()
What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

