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