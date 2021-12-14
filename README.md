# Python Brush Up 2021



Quiz: The Standard Library
Quiz: Compute an Exponent
It's your turn to import and use the math module. Use the math module to calculate e to the power of 3. print the answer.

Refer to the math module's documentation to find the function you need!

# print e to the power of 3 using the math module
  
Quiz: Password Generator
Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable word_list to build the password.

password_generator.py
words.txt
# TODO: First import the `random` module


# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces



# Now we test the function
print(generate_password())
  
Explore the Standard Library
In the following quizzes, enter the name of the module that solves each problem. Note that capitalization is important! Every module in the standard library is lowercased. You can browse the library documentation here.

Which Module? 1
Which module can tell you the current time and date?

Enter your response here
Which Module? 2
Which module has a method for changing the current working directory?

Enter your response here
Which Module? 3
Which module can read data from a comma separated values (.csv) file into Python dictionaries for each row?

Enter your response here
Which Module? 4
Which module can help extract all of the files from a zip file?

Enter your response here
Which Module? 5
Which module can say how long your code took to run?

Enter your response here
Our favourite modules
The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)



