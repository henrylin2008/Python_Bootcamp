filter
The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns True.

The function filter(function(),l) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns True will the element of the iterable be included in the result.

Lets see some examples:

In [4]:
#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True


Now let's filter a list of numbers. Note: putting the function into filter without any parenthesis might feel strange, but keep in mind that functions are objects as well.

In [3]:
lst =range(20)

filter(even_check,lst)
Out[3]:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


filter() is more commonly used with lambda functions, this because we usually use filter for a quick job where we don't want to write an entire function. Lets repeat the example above using a lambda expression:

In [5]:
filter(lambda x: x%2==0,lst)
Out[5]:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]