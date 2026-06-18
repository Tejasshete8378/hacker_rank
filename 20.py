"""
PROBLEM STATEMENT : Number Format Table Generator
---------------------------------------------------------------------------------------------
Objective:
Create a program that takes an integer input and displays a structured conversion table 
spanning four different number systems for all values from 1 up to that input.

Constraint:
1 <= number <= 99

Input:
A single integer entered by the user after an "Enter Number: " prompt.

Output:
A stylized "Welcome to the Program" banner, followed by a right-aligned table containing 
the decimal, octal, uppercase hexadecimal, and binary representations of each number, 
ending with a "Thank You" banner.

Task: 
Generate a table from 1 to N where each value is converted into four bases, padded with spaces 
to match the character width of the largest number's binary representation, and printed row 
by row between custom program headers.
"""

def print_formatted(number):
    if 1<=number<=99:
        max_binary_number = bin(number)[2:]
        width = len(max_binary_number)

        for i in range(1, number+1):
            print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")


if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    n = int(input("Enter Number: "))
    print_formatted(n)

    print('\n','*'*30,"Thank You",'*'*30,'\n')
