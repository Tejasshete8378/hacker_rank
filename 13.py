"""
PROBLEM STATEMENT : Custom Full Name Greeting with Length Validation 
---------------------------------------------------------------------------------------------
Objective:
Create a program that takes a user's first and last name as input and prints a personalized greeting message, provided both names meet specific length requirements.

Constraint:
- The length of the first name must be less than or equal to 10 characters: len(first_name) <= 10
- The length of the last name must be less than or equal to 10 characters: len(last_name) <= 10

Input:
- A string representing the first name.
- A string representing the last name.

Output:
- A welcome banner and input prompts.
- A personalized greeting if constraints are met: "Hello [first_name] [last_name]! You just delved into Python"
- An error message if constraints are violated: "First and Last Names should be 10 Characters or Less"
- A closing thank you banner.

Task:
Accept first and last names, validate that neither exceeds 10 characters, and output either a formatted greeting or a validation error within a styled terminal layout.

"""


def print_full_name(first_name, last_name):
    if len(first_name)<=10 and len(last_name)<=10:
        print(f"Hello {first_name} {last_name}! You just delved into Python")
        print()
    else:
        print(f"First and Last Names should be 10 Characters or Less")
        print()

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    first_name = input("Enter First Name: ")
    print()
    last_name = input("Enter Last Name: ")
    print()
    print_full_name(first_name, last_name)
    print('*'*30,"Thank You",'*'*30)
    print()
