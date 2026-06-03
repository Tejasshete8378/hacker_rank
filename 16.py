"""
PROBLEM STATEMENT : Interactive String Character Classifier
---------------------------------------------------------------------------------------------
Objective:
Develop a command-line utility that allows users to input a string and evaluate it for the 
presence of specific character classifications using structural string queries.

Constraint:
- The input string length must satisfy: 0 < len(data) < 1000.
- The user menu selection must be parsed as a numeric option from 1 to 6.

Input:
- A user-provided string (`s`) representing the target dataset.
- An integer (`choice`) indicating the validation routine to execute.

Output:
- A confirmation text block specifying whether the condition evaluates to True or False.
- Terminal boundaries marked with decorative separators (`*`).
- Error strings handling boundary exceptions or unrecognized choice inputs.

Task:
Design a control-flow system using Python's conditional statements and generator-driven 
any() functions to iterate through individual string components and evaluate the entire 
collection against user-selected criteria, exiting cleanly upon explicit signal.
"""

if __name__ == '__main__':
    import sys
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    s = input("Enter Data: ")
    print()
     
    choice = int(input("What Do you want to Check: "
    "\n1) Is Data contain any Alphanumeric Characters "
    "\n2) Is Data contain any Alphabetical Characters"
    "\n3) Is Data contain any Digit"
    "\n4) Is Data contain any Lowercase Characters"
    "\n5) Is Data contain any Uppercase Characters" \
    "\n6) Exit"
    "\n Please Enter your Choice: "))
    print()

    if choice == 6:
            print("\nThank You for using Program\n")
            sys.exit()
    
    elif 0<len(s)<1000:
        if choice == 1:
            if any(char.isalnum() for char in s):
                print("Entered Data contain Alphanumeric Characters\n")
            else:
                print("Entered Data does not contain any Alphanumeric Characters\n")

        elif choice == 2:
            if any(char.isalpha() for char in s):
                print("Entered Data contain Alphabetical Characters\n")
            else:
                print("Entered Data does not contain any Alphabetical Characters\n")

        elif choice == 3:
            if any(char.isdigit() for char in s):
                print("Entered Data contain Digits\n")
            else:
                print("Entered Data does not contain any Digits\n")

        elif choice == 4:
            if any(char.islower() for char in s):
                print("Entered Data contain Lowercase Characters\n")
            else:
                print("Entered Data does not contain any Lowercase Characters\n")

        elif choice == 5:
            if any(char.isupper() for char in s):
                print("Entered Data contain Uppercase Characters\n")
            else:
                print("Entered Data does not contain any Uppercase Characters\n")
           
        else: 
            print("Please Enter Valid Choice!!!\n")
    
    else: 
        print("Data limit exceeded. Please enter Data of size less than 1000 Characters")
        
    print('*'*30,"Thank You",'*'*30,'\n')