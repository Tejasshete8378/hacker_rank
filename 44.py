"""
PROBLEM STATEMENT : Sum of Powers Calculator 
---------------------------------------------------------------------------------------------
Objective:
--------------

To calculate and display the sum of two numbers, each raised to their respective independent powers, 
based on user input.

Constraint:
--------------

Inputs must be valid integers.
Calculations involve standard arithmetic power operations.

Input:
--------------

An integer representing the first base number (a).
An integer representing the power for the first number (b).
An integer representing the second base number (c).
An integer representing the power for the second number (d).

Output:
--------------

The calculated result of the expression (a raised to b plus c raised to d) formatted in a descriptive output string.

Task:
--------------

Take four integer inputs from the user for two pairs of base numbers and their corresponding exponents, 
compute the sum of their powered values, and print the final result.

"""

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    a = int(input("Enter First Number: "))
    print()
    b = int(input("Enter Power of First Number: "))
    print()
    c = int(input("Enter Second Number: "))
    print()
    d = int(input("Enter Power of Second Number: "))
    print()

    result = a**b + c**d

    print(f"Sum of {a} power {b} and {c} power {d}: {result}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')