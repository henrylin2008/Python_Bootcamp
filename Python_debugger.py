Python Debugger
You've probably used a variety of print statements to try to find errors in your code. A better way of doing this is by using Python's built-in debugger module (pdb). The pdb module implements an interactive debugging environment for Python programs. It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.

This is a bit difficult to show since it requires creating an error on purpose, but hopefully this simple example illustrates the power of the pdb module. Note: Keep in mind it would be pretty unusual to use pdb in an iPython Notebook setting.

Here we will create an error on purpose, trying to add a list to an integer

In [3]:
x = [1,3,4]
y = 2
z = 3

result = y + z
print result
result2 = y+x
print result2
5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-a207358d437b> in <module>()
      5 result = y + z
      6 print result
----> 7 result2 = y+x
      8 print result2

TypeError: unsupported operand type(s) for +: 'int' and 'list'
