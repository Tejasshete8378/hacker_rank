"""
PROBLEM STATEMENT : Case Transformation Utility
---------------------------------------------------------------------------------------------
Objective:
Design a program that toggles the case of every alphabetic character in a given 
string, converting uppercase letters to lowercase and vice versa.

Constraint:
- The input string 's' must have a length between 1 (inclusive) and 1000 (inclusive).
- Non-alphabetic characters (numbers, symbols, spaces) must remain unchanged.
- The logic should be encapsulated within a specific function.

Input:
- A single string 's' entered by the user via the command line.

Output:
- A decorative welcome message.
- The transformed string where all cases are swapped.
- A decorative closing message.

Task:
Implement a function named swap_case that validates the string length and 
returns the case-swapped version of the input. Use a main block to handle user 
interaction and display the result.
"""

def swap_case(s):
    if 0<len(s)<=1000:
        new_output = s.swapcase()
    return new_output

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    
    s = input("Enter String: ")
    print()
    result = swap_case(s)
    print(f"Swapped String: {result}")
    
    print()
    print('*'*30,"Thank You",'*'*30)
    print()