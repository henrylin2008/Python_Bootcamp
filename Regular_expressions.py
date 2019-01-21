
Regular Expressions
Regular expressions are text matching patterns described with a formal syntax. You'll often hear regular expressions referred to as 'regex' or 'regexp' in conversation. Regular expressions can include a variety of rules, fro finding repetition, to text-matching, and much more. As you advance in Python you'll see that a lot of your parsing problems can be solved with regular expressions (they're also a common interview question!).

If you're familiar with Perl, you'll notice that the syntax for regular expressions are very similar in Python. We will be using the re module with Python for this lecture.

Let's get started!

Searching for Patterns in Text
One of the most common uses for the re module is for finding patterns in text. Let's do a quick example of using the search method in the re module to find some text:

In [8]:
import re

# List of patterns to search for
patterns = [ 'term1', 'term2' ]

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print 'Searching for "%s" in: \n"%s"' % (pattern, text),
    
    #Check for match
    if re.search(pattern,  text):
        print '\n'
        print 'Match was found. \n'
    else:
        print '\n'
        print 'No Match was found.\n'

Searching for "term1" in: 
"This is a string with term1, but it does not have the other term." 

Match was found. 

Searching for "term2" in: 
"This is a string with term1, but it does not have the other term." 

No Match was found.

Now we've seen that re.search() will take the pattern, scan the text, and then returns a Match object. If no pattern is found, a None is returned. To give a clearer picture of this match object, check out the cell below:

In [15]:
# List of patterns to search for
pattern = 'term1'

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern,  text)

type(match)
Out[15]:
_sre.SRE_Match


This Match object returned by the search() method is more than just a Boolean or None, it contains information about the match, including the original input string, the regular expression that was used, and the location of the match. Let's see the methods we can use on the match object:

In [21]:
# Show start of match
match.start()
Out[21]:
22
In [23]:
# Show end
match.end()
Out[23]:
27


Split with regular expressions
Let's see how we can split with the re syntax. This should look similar to how you used the split() method with strings.

In [25]:
# Term to split on
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Split the phrase
re.split(split_term,phrase)
Out[25]:
['What is the domain name of someone with the email: hello', 'gmail.com']
Note how re.split() returns a list with the term to spit on removed and the terms in the list are a split up version of the string. Create a couple of more examples for yourself to make sure you understand!

