if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    s = input("Enter Data:")
    print()
    choice = int(input("What Do you want to Check: "
    "/n1) Is Data contain any Alphanumeric Characters "
    "/n2) Is Data contain any Alphabetical Characters"
    "/n3) Is Data contain any Digit"
    "/n4) Is Data contain any Lowercase Characters"
    "/n5) Is Data contain any Uppercase Characters"))
    if 0<len(s)<1000:
        if choice == 1:
            print(any(char.isalnum() for char in s))
        if choice == 2:
            print(any(char.isalpha() for char in s))
        if choice == 3:
            print(any(char.isdigit() for char in s))
        if choice == 4:
            print(any(char.islower() for char in s))
        if choice == 5:
            print(any(char.isupper() for char in s))