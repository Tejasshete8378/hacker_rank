"""
PROBLEM STATEMENT : Power and Modulo Calculation Tool
---------------------------------------------------------------------------------------------
Objective:
--------------
To compute the power of a given number raised to an exponent, and optionally calculate the modulo of the result with respect to a third number, 
handling potential division by zero errors for the modulo operation.

Constraint:
--------------
- The divisor for the modulo operation must not be zero (c != 0).

Input:
--------------
- An integer a representing the base number.
- An integer b representing the exponent/power.
- An integer c representing the number to find the modulo with.

Output:
--------------
- The calculated power value (a^b).
- The modulo value (a^b % c) if c != 0, or an error message if c == 0.

Task:
--------------
Write a program that takes three integer inputs (base, exponent, and mod value), computes the power of the base to the exponent, 
calculates the modulo of that power against the third number (handling zero-division gracefully), and displays the formatted results.
"""

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    a = int(input("Enter the Number whose Power do you want to find: "))
    print()
    b = int(input("Enter Power: "))
    print()
    c = int(input("Enter Number to find Mod: "))
    print()

    result1 = pow(a,b)

    print(f"Power of {a} and {b} is: {result1}\n")

    if c != 0:
            result2 = pow(a,b,c)
            print(f"Mod: {result2}")
    else:
        print("Mod Error! Division or Mod by 0 is not allowed \n")
    

    print('\n','*'*30,"Thank YOu",'*'*30,'\n')