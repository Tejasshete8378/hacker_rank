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

