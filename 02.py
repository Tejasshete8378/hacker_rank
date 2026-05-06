"""
PROBLEM STATEMENT: Functional Arithmetic with Formatted Output
--------------------------------------------------------------
Objective:
Create a script that accepts two large integers as input and 
calculates their sum, difference, and product using dedicated 
modular functions.

Constraints:
1. Input Range: Ensure both integers 'a' and 'b' fall within 
   the range: 1 <= a, b <= 10^10.
2. Logic: The operations must only execute if the inputs meet 
   the specified constraints.

Task:
- Prompt the user for two integer inputs with descriptive labels.
- Implement three functions: summation(), subtraction(), and multiplication().
- Display the results using f-string formatting to provide 
  clear, labeled output for each calculation.
"""

def summation(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b
    
if __name__ == '__main__':
        print('*'*30,"Welcome to the Program",'*'*30)
        print()
        a = int(input("Enter First Number: "))
        print()
        b = int(input("Enter Second Number: "))
        print()

        if (1<=a<=10**10) and (1<=b<=10**10):
            print(f"Addition of Two Numbers = {summation(a,b)}")
            print()
            print(f"Substraction of Two Numbers = {subtraction(a,b)}")
            print()
            print(f"Multiplication of Two Numbers = {multiplication(a,b)}")
print()
print('*'*30,"Thank You",'*'*30)