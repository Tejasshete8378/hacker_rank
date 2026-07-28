"""
PROBLEM STATEMENT : Interactive Division and Modulo Calculator
---------------------------------------------------------------------------------------------
Objective:
--------------
To take two user-provided integer inputs and compute their integer division, modulus, and combined divmod tuple, displaying the results in a formatted, 
user-friendly interactive interface.

Constraint:
--------------
Inputs must be valid integers. The second integer must not be zero to prevent division by zero errors.

Input:
--------------
Two integers provided via standard input (interactive prompts).

Output:
--------------
Formatted text displaying the welcome banner, calculation results for integer division, modulo, and divmod, followed by a thank you banner.

Task:
--------------
Write a Python script that prompts the user for two numbers, calculates their integer division, remainder, and divmod, and prints the descriptive outputs 
cleanly with decorative banners.

"""


if __name__ == '__main__':
    print('\n','*'*30, "Welcome to the Program",'*'*30,'\n')
    a = int(input("Enter First Number: "))
    print()
    b = int(input("Enter Second Number: "))
    print()

    int_div = a//b
    mod_div = a%b
    div_mod = divmod(a,b)

    print(f"Integer Division = {int_div}\n")
    print(f"Modulo Division = {mod_div}\n")
    print(f"Divmod = {div_mod}\n")

    print('\n','*'*30, "Thank You",'*'*30,'\n')