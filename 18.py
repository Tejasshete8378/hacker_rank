"""
PROBLEM STATEMENT : Text Wrap Utility
---------------------------------------------------------------------------------------------
Objective:
Wrap a given string into a paragraph of a specified maximum width using a text wrapping utility.

Constraint:
- 0 < length of string < 1000
- 0 < max_width < length of string

Input:
- A single string containing characters, spaces, or symbols.
- An integer representing the maximum width allowed for each line of text.

Output:
- The input string broken into multiple lines, where no line exceeds the maximum width.

Task: 
Take a string and a width value from the user, validate that both fit within the size constraints, 
wrap the text accordingly, and display the result.

"""


import textwrap

def wrap(string, max_width):
    if 0<len(string)<1000 and 0<max_width<len(string):
        result = textwrap.fill(string, max_width)
        return result

if __name__ == '__main__':

    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    string = input("Enter String: ")
    max_width = int(input("\nEnter Width to Wrap: "))
    
    result = wrap(string, max_width)
    print(f"\nWrapped Text: \n{result}")
    
    print('\n','*'*30,"Thank You",'*'*30,'\n')
