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

In [7]:
print globals()
{'_dh': [u'/Users/marci/Udemy-Complete-Python-Bootcamp'], '__': '', '_i': u"s = 'Global Variable'\n\ndef func():\n    print locals()", 'quit': <IPython.core.autocall.ZMQExitAutocall object at 0x1037e0a10>, '__builtins__': <module '__builtin__' (built-in)>, 's': 'Global Variable', '_ih': ['', u'def func():\n    return 1', u'func()', u"s = 'Global Variable'\n\ndef func():\n    print locals()", u'print globals()', u'print globals().keys()', u"s = 'Global Variable'\n\ndef func():\n    print locals()", u'print globals()'], '__builtin__': <module '__builtin__' (built-in)>, '_2': 1, 'func': <function func at 0x10445aa28>, '__name__': '__main__', '___': '', '_': 1, '_sh': <module 'IPython.core.shadowns' from '//anaconda/lib/python2.7/site-packages/IPython/core/shadowns.pyc'>, '_i7': u'print globals()', '_i6': u"s = 'Global Variable'\n\ndef func():\n    print locals()", '_i5': u'print globals().keys()', '_i4': u'print globals()', '_i3': u"s = 'Global Variable'\n\ndef func():\n    print locals()", '_i2': u'func()', '_i1': u'def func():\n    return 1', '__doc__': 'Automatically created module for IPython interactive environment', '_iii': u'print globals()', 'exit': <IPython.core.autocall.ZMQExitAutocall object at 0x1037e0a10>, 'get_ipython': <bound method ZMQInteractiveShell.get_ipython of <IPython.kernel.zmq.zmqshell.ZMQInteractiveShell object at 0x1037c3990>>, '_ii': u'print globals().keys()', 'In': ['', u'def func():\n    return 1', u'func()', u"s = 'Global Variable'\n\ndef func():\n    print locals()", u'print globals()', u'print globals().keys()', u"s = 'Global Variable'\n\ndef func():\n    print locals()", u'print globals()'], '_oh': {2: 1}, 'Out': {2: 1}}
Here we get back a dictionary of all the global variables, many of them are predefined in Python. So let's go ahead and look at the keys:

In [8]:
print globals().keys()
['_dh', '__', '_i', 'quit', '__builtins__', 's', '_ih', '__builtin__', '_2', 'func', '__name__', '___', '_', '_sh', '_i8', '_i7', '_i6', '_i5', '_i4', '_i3', '_i2', '_i1', '__doc__', '_iii', 'exit', 'get_ipython', '_ii', 'In', '_oh', 'Out']