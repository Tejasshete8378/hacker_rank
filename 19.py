"""
PROBLEM STATEMENT: Symmetric Door Mat Design Generator with Input Validation
---------------------------------------------------------------------------------------------
Objective:
Create a Python program that generates a symmetric ASCII art door mat pattern based on 
a size value provided by the user.

Constraints:
- The total grid width (M) must be exactly three times the given height (N), so M = N * 3.
- The height value (N) must be a positive, odd integer greater than zero.

Input:
- An integer value typed by the user representing the height (N).
- The program must continuously ask for input if the user enters an invalid number.
- It must handle and reject negative even numbers, positive even numbers, negative odd 
  numbers, and zero with specific error messages.

Output:
- A welcome message wrapped in 30 stars at the start.
- A top pattern of triangles made of repeated ".|." symbols centered with hyphens "-".
- A center line with the word "Welcome" centered with hyphens "-".
- A bottom pattern made of repeated ".|." symbols that mirrors the top half.
- A thank you message wrapped in 30 stars at the very end.

Task:
Build an interactive script that validates user input for specific mathematical rules 
and uses string repetition alongside text centering methods to print a balanced, 
decorative text pattern.
"""


if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')

    

    while True:
        N = int(input("Enter Odd Positive Natural Number: "))
        print()
        
        if N%2 == 0 and N<0:
            print(f"{N} is a Negative Even Number! Please try again.\n")
        elif N%2 == 0: 
            print(f"{N} is an Even Number! Please try again.\n")
        elif N<0:
            print(f"{N} is a Negative Number! Please try again.\n") 
        elif N==0:
            print(f"{N} is Zero! Natural Numbers should be greater than Zero.\n")    
        else:
            break
    
    M = N*3

    for i in range(1, N, 2):
        print((i*".|.").center(M, "-"))

    print("Welcome".center(M, "-"))

    for i in range(N-2, -1, -2):
        print((i*".|.").center(M, "-"))
    
    print('\n','*'*30,"Thank You",'*'*30,'\n')

