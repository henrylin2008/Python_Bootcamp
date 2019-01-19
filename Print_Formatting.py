Print Formatting
In this lecture we will briefly cover the various ways to format your print statements. As you code more and more, you will probably want to have print statements that can take in a variable into a printed string statement.

The most basic example of a print statement is:

In [17]:
print 'This is a string'
This is a string

Strings
You can use the %s to format strings into your print statements.

In [4]:
s = 'STRING'
print 'Place another string with a mod and s: %s' %(s)
Place another string with a mod and s: STRING

Floating Point Numbers
Floating point numbers use the format %n1.n2f where the n1 is the total minimum number of digits the string should contain (these may be filled with whitespace if the entire number does not have this many digits. The n2 placeholder stands for how many numbers to show past the decimal point. Lets see some examples:

In [12]:
print 'Floating point numbers: %1.2f' %(13.144)
Floating point numbers: 13.14
In [13]:
print 'Floating point numbers: %1.0f' %(13.144)
Floating point numbers: 13
In [14]:
print 'Floating point numbers: %1.5f' %(13.144)
Floating point numbers: 13.14400
In [15]:
print 'Floating point numbers: %10.2f' %(13.144)
Floating point numbers:      13.14
In [19]:
print 'Floating point numbers: %25.2f' %(13.144)
Floating point numbers:                     13.14
