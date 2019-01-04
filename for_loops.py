for Loops
A for loop acts as an iterator in Python, it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings,lists,tuples, and even built in iterables for dictionaries, such as the keys or values.

We've already seen the for statement a little bit in past lectures but now lets formalize our understanding.

Here's the general format for a for loop in Python:

for item in object:
    statements to do stuff


The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside you loop, for example if you wanted to use if statements to perform checks.

Let's go ahead and work through several example of for loops using a variety of data object types. we'll start simple and build more complexity later on.

Example 1
Iterating through a list.

In [1]:
# We'll learn how to automate this sort of list in the next lecture
l = [1,2,3,4,5,6,7,8,9,10]
In [2]:
for num in l:
    print num
1
2
3
4
5
6
7
8
9
10
Great! Hopefully this makes sense. Now lets add a if statement to check for even numbers. We'll first introduce a new concept here--the modulo.


Modulo
The modulo allows us to get the remainder in a division and uses the % symbol. For example:

In [5]:
17 % 5
Out[5]:
2
This makes sense since 17 divided by 5 is 3 remainder 2. Let's see a few more quick examples:

In [6]:
# 3 Remainder 1
10 % 3
Out[6]:
1
In [9]:
# 2 Remainder 4
18 % 7
Out[9]:
4
In [10]:
# 2 no remainder
4 % 2
Out[10]:
0
Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!

Back to the for loops!


Example 2
Let's print only the even numbers from that list!

In [11]:
for num in l:
    if num % 2 == 0:
        print num
2
4
6
8
10

We could have also put in else statement in there:

In [12]:
for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'Odd number'
Odd number
2
Odd number
4
Odd number
6
Odd number
8
Odd number
10

Example 3
Another common idea during a for loop is keeping some sort of running tally during the multiple loops. For example, lets create a for loop that sums up the list:

In [13]:
# Start sum at zero
list_sum = 0 

for num in l:
    list_sum = list_sum + num

print list_sum
55
Great! Read over the above cell and make sure you understand fully what is going on. Also we could have implemented a += to to the addition towards the sum. For example:

In [14]:
# Start sum at zero
list_sum = 0 

for num in l:
    list_sum += num

print list_sum
55


Example 4
We've used for loops with lists, how about with strings? Remember strings are a sequence so when we iterate through them we will be accessing each item in that string.

In [15]:
for letter in 'This is a string.':
    print letter
T
h
i
s
 
i
s
 
a
 
s
t
r
i
n
g
.