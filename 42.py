"""
PROBLEM STATEMENT : Division Calculator with Error Handling and Formatting
---------------------------------------------------------------------------------------------
Objective:
--------------
To take two integer inputs from the user, perform both integer and float division, and display the results cleanly while handling potential runtime exceptions.

Constraint:
--------------
- The second input number must not be zero (to avoid division by zero).
- Inputs must be valid integer numbers.

Input:
--------------
- Two integer values entered sequentially via standard input (`a` and `b`).

Output:
--------------
- A welcome banner at the start.
- The result of integer division (`a // b`).
- The result of standard float division (`a / b`).
- Error messages if invalid inputs or division by zero occur.
- A thank you banner at the end.

Task:
--------------
Write a Python program that prompts the user for two integers, calculates their integer and float division, 
handles exceptions gracefully if the user enters non-integer values or tries to divide by zero, and formats the output with descriptive welcome and thank-you banners.

"""



if __name__ == '__main__':
    print('\n','*'*30, "Welcome to the Program",'*'*30,'\n')
    try:
        a = int(input("Enter First Number: "))
        print()
        b = int(input("Enter Second Number: "))
        print()
    
        int_div = a//b
        float_div = a/b

        print(f"Integer Division = {int_div}\n")
        print(f"Float Division = {float_div}")
    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed\n")
    except ValueError:
        print("Error: Please Enter Valid Numbers")

    print('\n','*'*30,"Thank You",'*'*30,'\n')