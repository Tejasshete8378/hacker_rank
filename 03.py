"""
PROBLEM STATEMENT : Dual Arithmetic Division Processing
---------------------------------------------------------------------------------------------
Objective:
Create a program that accepts two integer inputs and calculates both the 
truncated integer quotient and the precise floating-point result using 
modular functions.

Constraint:
1. Inputs must be captured as integers via console input.
2. The program must include a safety check to ensure the divisor is not zero 
   before attempting calculations.
3. Division logic must be separated into distinct functions rather than 
   being performed directly in the main block.

Task:
1. Define a function `intdiv(a, b)` that returns the integer result of division.
2. Define a function `floatdiv(a, b)` that returns the float result of division.
3. Implement a main execution block to handle user input and output.
4. Output the results in two lines: integer division first, then float division.
"""

def intdiv (a,b):
    return int(a/b)
def floatdiv (a,b):
    return float(a/b)

if __name__ == '__main__':
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    
    if b != 0:
        print(f"Integer Division of {a} and {b}: {intdiv(a,b)}")
        print(f"Float Division of {a} and {b}: {floatdiv(a,b)}")