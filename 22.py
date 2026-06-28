"""
PROBLEM STATEMENT : Word Capitalization Utility
---------------------------------------------------------------------------------------------
Objective:
----------
Convert a given input string into a format where the first character of every word 
is capitalized and the remaining characters are lowercase.

Constraint:
-----------
The solution must handle varying amounts of whitespace (leading, trailing, 
or multiple spaces between words) gracefully.

Input:
------
A single string 's' containing one or more words separated by whitespace.

Output:
-------
A single string with each word correctly capitalized, separated by a single space.

Task:
------
Implement a function that tokenizes the input string regardless of extra 
whitespace, capitalizes each token, and joins them back into a clean string.
"""


def solve(s):
    # Using .split() without the " " argument is a common Python trick to ignore 
    # all extra whitespace automatically.
    words = s.split()
    capitalize_word = [word.capitalize() for word in words]
    return " ".join(capitalize_word)

if __name__ == '__main__':
    print('\n',"*"*30,"Welcome to the Program","*"*30,'\n')
    text = input("Enter Text: ")
    print()
    result = solve(text)
    print(f"Capitalized Text: {result}")
    print('\n',"*"*30,"Thank You","*"*30,'\n')