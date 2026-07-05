
def average(arr):
    s = set(arr)
    setsum = sum(s)
    totalnum = len(s)
    avg = setsum/totalnum
    return avg

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    n = int(input("Enter How many Numbers average do you want to calculate: "))
    print()
    arr = list(map(int, input("Enter Numbers:").split()))
    print()
    
    if len(arr) < n:
        print(f"You have entered only {len(arr)} Numbers, Please enter {n - len(arr)} more Numbers")
    elif len(arr) > n:
        print(f"You have entered {len(arr)} Numbers, Please enter {n} Numbers only")
    elif len(arr) == 0:
        print("Please Enter Number")
    else:
        result = average(arr)
    
    print(f"Average : {result}")
    print('\n','*'*30,"Thank You",'*'*30,'\n')