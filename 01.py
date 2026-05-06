"""
PROBLEM STATEMENT: Conditional Logic Evaluation ("Weird" vs "Not Weird")
-----------------------------------------------------------------------
Objective:
Given an integer n, perform specific conditional actions to determine 
if the number is classified as "Weird" or "Not Weird" based on its 
parity and range.

Constraints:
1. If n is odd, print "Weird".
2. If n is even and in the inclusive range of 2 to 5, print "Not Weird".
3. If n is even and in the inclusive range of 6 to 20, print "Weird".
4. If n is even and greater than 20, print "Not Weird".

Task:
Implement a function that evaluates these conditions using if-elif-else 
statements and handle user input via the standard input stream.
"""

def operation(n):
    if n%2 != 0:
        print("Weird")
    elif 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    n = int(input("Enter Number: ").strip())
    print()
    operation(n)

print()
print('*'*30,"Thank You",'*'*30)