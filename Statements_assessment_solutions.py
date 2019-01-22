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
