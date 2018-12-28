The collections module is a built-in module that implements specialized container data types providing alternatives to Python’s general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.

Now we'll learn about the alternatives that the collections module provides.

Counter
Counter is a dict subclass which helps count hash-able objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

Lets see how it can be used:

In [1]:
from collections import Counter
Counter() with lists

In [2]:
l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

Counter(l)
Out[2]:
Counter({1: 6, 2: 6, 3: 4, 32: 1, 12: 1, 21: 1, 223: 1})


Counter with strings

In [3]:
Counter('aabsbsbsbhshhbbsbs')
Out[3]:
Counter({'b': 7, 's': 6, 'h': 3, 'a': 2})

Counter with words in a sentence

In [4]:
s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

Counter(words)
Out[4]:
Counter({'word': 3, 'each': 3, 'times': 2, 'show': 1, 'this': 1, 'many': 1, 'in': 1, 'up': 1, 'How': 1, 'does': 1, 'sentence': 1})
In [5]:
# Methods with Counter()
c = Counter(words)

c.most_common(2)
Out[5]:
[('word', 3), ('each', 3)]