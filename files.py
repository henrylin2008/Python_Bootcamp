Files
Python uses file objects to interact with external files on your computer. These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails, Excel documents, etc. Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily available. (We will cover downloading modules later on in the course).

Python has a built-in open function that allows us to open and play with basic file types. First we will need a file though. We're going to use some iPython magic to create a text file!

iPython Writing a File
In [6]:
%%writefile test.txt
Hello, this is a quick test file
Overwriting test.txt

Python Opening a file
We can open a file with the open() function. The open function also takes in arguments (also called parameters). Lets see how this is used:

In [14]:
# Open the text.txt we made earlier
my_file = open('test.txt')
In [15]:
# We can now read the file
my_file.read()
Out[15]:
'Hello, this is a quick test file'
In [16]:
# But what happens if we try to read it again?
my_file.read()
Out[16]:
''