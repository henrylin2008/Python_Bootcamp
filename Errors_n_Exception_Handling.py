In this lecture we will learn about Errors and Exception Handling in Python. You've definitely already encountered errors by this point in the course. For example:

In [1]:
print 'Hello
  File "<ipython-input-1-23e01f0d17c8>", line 1
    print 'Hello
               ^
SyntaxError: EOL while scanning string literal
Note how we get a SyntaxError, with the further description that it was an EOL (End of Line Error) while scanning the string literal. This is specific enough for us to see that we forgot a single quote at the end of the line. Understanding these various error types will help you debug your code much faster.

This type of error and description is known as an Exception. Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal.

You can check out the full list of built-in exceptions here. now lets learn how to handle errors and exceptions in our own code.


try and except
The basic terminology and syntax used to handle errors in Python is the try and except statements. The code which can cause an exception to occue is put in the try block and the handling of the exception is the implemented in the except block of code. The syntax form is:

try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 

We can also just check for any exception with just using except: To get a better understanding of all this lets check out an example: We will look at some code that opens and writes a file:

In [11]:
try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written successfully"
   f.close()
Content written successfully
Now lets see what would happen if we did not have write permission (opening only with 'r'):

In [14]:
try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written successfully"
   f.close()
Error: Could not find file or read data