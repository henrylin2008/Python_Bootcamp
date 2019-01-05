Write a function that computes the volume of a sphere given its radius.

In [25]:
def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)
Write a function that checks whether a number is in a given range (Inclusive of high and low)

In [7]:
def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):  
        print " %s is in the range" %str(num)  
    else :  
        print "The number is outside the range."
If you only wanted to return a boolean:

In [8]:
def ran_bool(num,low,high):
    return num in range(low,high+1)
In [9]:
ran_bool(3,1,10)
Out[9]:
True