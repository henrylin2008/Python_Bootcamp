Hexadecimal
Using the function hex() you can convert numbers into a hexadecimal format:

In [4]:
hex(246)
Out[4]:
'0xf6'
In [5]:
hex(512)
Out[5]:
'0x200'


Binary
Using the function bin() you can convert numbers into their binary format.

In [19]:
bin(1234)
Out[19]:
'0b10011010010'
In [18]:
bin(128)
Out[18]:
'0b10000000'
In [16]:
bin(512)
Out[16]:
'0b1000000000'


pow()
With two arguments, equivalent to x^y. With three arguments, equivalent to (x^y) % z, but may be more efficient (e.g. for longs).

In [8]:
pow(2,4)
Out[8]:
16



abs
Absolute Value

In [9]:
abs(-3)
Out[9]:
3
In [10]:
abs(3)
Out[10]:
3