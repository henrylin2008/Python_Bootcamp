Statements Assessment Solutions
Use for, split(), and if to create a Statement that will print out words that start with 's':

In [3]:
st = 'Print only the words that start with s in this sentence'
In [4]:
for word in st.split():
    if word[0] == 's':
        print word
start
s
sentence


Use range() to print all the even numbers from 0 to 10.

In [1]:
range(0,11,2)
Out[1]:
[0, 2, 4, 6, 8, 10]


Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

In [1]:
[x for x in range(1,50) if x%3 == 0]
Out[1]:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


Go through the string below and if the length of a word is even print "even!"

In [2]:
st = 'Print every word in this sentence that has an even number of letters'
In [4]:
for word in st.split():
    if len(word)%2 == 0:
        print word+" <-- has an even length!"
word <-- has an even length!
in <-- has an even length!
this <-- has an even length!
sentence <-- has an even length!
that <-- has an even length!
an <-- has an even length!
even <-- has an even length!
number <-- has an even length!
of <-- has an even length!

Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

In [ ]:
for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num