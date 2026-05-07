"""
PROBLEM STATEMENT : Spaced Sequential Integer Generator
---------------------------------------------------------------------------------------------
Objective:
Develop a program that displays a sequence of integers from 1 to 'n' with consistent 
spacing between each number, framed by decorative console banners.

Constraint:
n should be a positive integer.

Input:
A user-defined integer 'n'.

Output:
- A "Welcome" header centered between asterisk borders.
- A labeled line showing integers 1 through n, separated by single spaces.
- A "Thank You" footer separated from the results by visual padding.

Task:
Read an input 'n', then use a while loop to print the sequence 1 to n. Use the 
'end' parameter to maintain single-line output with spaces, and ensure 
proper vertical spacing before the closing banner.
"""



print('*'*30,"Welcome to the Program",'*'*30)
print()
if __name__ == '__main__':
    n = int(input("Enter Number: "))
    print()
    
    i = 1
    print(f"Sequential integers upto {n} are: ", end = '')
    while i <= n:
        print(i, end = ' ')
        i += 1
print()      
print()
print('*'*30,"Thank You",'*'*30)