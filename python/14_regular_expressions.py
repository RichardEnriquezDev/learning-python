
### Regular Expressions ###
""" A regular expression or RegEx is a special text string
    that helps to find patterns in data."""

# First import re
import re

# Match
# re.match(): searches only in the beginning of the first line
# of the string and returns matched objects if found, else returns None.
text = "I am learning the Python programming language. Of all programming languages, it is the  easiest to learn."
match = re.match("I am learning", text, re.I)
print(match)

# Search
# Returns a match object if there is one anywhere in the string,
# including multiline strings.
search = re.search("languages", text, re.I)
print(search) #Search returns a match object with a first match
# that was found.

# Findall 
# returns all the matches as a list
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''
findall = re.findall("language", text, re.I)
print(findall)
# re.I:
# Since we are using re.I both lowercase and uppercase letters are included.

# Re.sub
# replace word
word_replace = re.sub("Python|python", "Java", txt, re.I)
print(word_replace)
# Example to use
text = "-I-am-learning-the-Python-programming-language. Of-all-programming-languages, it-is-the-easiest-to-learn.-"
word_replace = re.sub("-", ' ', text)
print(word_replace)

# Split:
# Takes a string, splits it at the match points, returns a list
txt = """I am learning the Python programming Language.
Of all programming languages, it is the  easiest to learn.
Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""
string_split = re.split('\n', txt)
print(string_split)

# RegEX Patterns
regex_patterns = r"beautiful"
matches = re.findall(regex_patterns, txt) # for case insensitive adding flags, example re.I.
print("it was found:",matches)

# Others expressions
""" [], '\', ., ^, $, *, +, ?, {}, |, ()."""

regex_patterns = r"[Ll]anguage" # [] upper and lower case
matches = re.findall(regex_patterns, txt)
print("it was found:",matches)

regex_patterns = r"[Ll]anguage|[Pp]rogramming" # with either
matches = re.findall(regex_patterns, txt)
print("it was found:",matches)

# Escape character '\'
txt = "'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'"
regex_patterns = r"\d" # d is a special character which means digits
matches = re.findall(regex_patterns, txt)
print("it was found:",matches)

# Character '+'
regex_patterns = r"\d+" # + mean one or more time
matches = re.findall(regex_patterns, txt)
print("it was found:",matches)

# Period '.'
regex_patterns = r"[a]." # '.' means any  character except new line, [a] find character 'a'.
matches = re.findall(regex_patterns, txt)
print("it was found:",matches)

regex_patterns = r"[a].+" # '+' means any character one or more times
matches = re.findall(regex_patterns, txt)
print("it was found:",matches)

# Zero or one time (?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print("it was found:",matches)

# Quantifier {}
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r'\d{4}'# exactly four times
matches = re.findall(regex_pattern, txt)
print("it was found:",matches)

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print("it was found:",matches)

# Cart ^
regex_pattern = r'^This' # '^' mean star with
matches = re.findall(regex_pattern, txt)
print("it was found:",matches)

regex_pattern = r'[^A-Za-z ]+' # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print("it was found:",matches)
