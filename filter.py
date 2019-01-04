filter
The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns True.

The function filter(function(),l) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns True will the element of the iterable be included in the result.

Lets see some examples:

In [4]:
#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True

