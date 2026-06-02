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