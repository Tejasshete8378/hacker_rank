"""
PROBLEM STATEMENT : Non-Negative Integer Squaring Logic
---------------------------------------------------------------------------------------------
Objective:
To iterate through a series of integers starting from zero and calculate the 
mathematical square of each value up to a user-defined limit.

Constraint:
- The loop must run while the counter 'i' is strictly less than input 'n'.
- Implementation must utilize a 'while' loop with a manual increment of the counter.
- The program must handle integer inputs and provide visual spacing in the console.

Input:
- A single integer 'n' representing the number of iterations.

Output:
- Decorative banners at the start and end of the execution.
- The square of each integer 'i' ($i^2$) displayed with vertical padding.

Task:
Initialize a counter and use a while loop to print the square of each incrementing 
integer until the specified limit is reached.
"""

if __name__ == '__main__':
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    n = int(input("Enter Number: "))
    i = 0
    
    while i<n:
        print()
        print(f"Square of {i}: {i**2}")
        print()
        i += 1
print('*'*30,"Thank You",'*'*30)