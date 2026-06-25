"""
PROBLEM STATEMENT : Enhanced Alphabet Rangoli Pattern Generator
---------------------------------------------------------------------------------------------
Objective:
To generate an N-size symmetric Rangoli pattern using lowercase English alphabet letters, wrapped in a formatted UI 
with greeting and exit messages.

Constraint:
0 < N < 27

Input:
A single integer N representing the size of the pattern.

Output:
A visually formatted console display featuring a welcome header, the generated alphabet Rangoli pattern, and a 
thank-you footer.

Task:
Implement a program that accepts an integer size, calculates the string slicing for the alphabet pattern, 
centers the output with dash padding, and surrounds the result with decorative asterisks.
"""

import string

def print_rangoli(size):
    chars = string.ascii_lowercase

    lines = []

    for i in range (size):
        s = "-".join(chars[size - 1:i:-1] + chars[i:size])
        lines.append(s.center(4*size - 3, "-"))

    rangoli = "\n".join(lines[::-1] + lines[1:])
    print(rangoli)

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    n = int(input("Enter Size: "))
    print()
    print_rangoli(n)
    print('\n','*'*30,"Thank You",'*'*30,'\n')


