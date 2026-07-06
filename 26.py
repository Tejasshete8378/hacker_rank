"""
PROBLEM STATEMENT : Calculate Average of Unique Elements
---------------------------------------------------------------------------------------------
Objective:
--------------
Create a program that accepts a specific count of integers from the user, identifies the unique values 
among them, and calculates their arithmetic mean.

Constraint:
--------------
- The number of inputs provided by the user must exactly match the expected count specified at the start.
- If the input array is empty, the program should handle it gracefully.
- The average must be calculated only using unique elements from the provided list.

Input:
--------------
- An integer `n` representing the expected number of inputs.
- A list of `n` space-separated integers.

Output:
--------------
- If valid inputs are provided, return the average of the unique elements as a float.
- If the set of unique elements has a sum of zero or is empty, print a message indicating the sum is zero and return 0.
- If the number of inputs provided does not match `n`, display an error message requesting the correct number of inputs.

Task:
--------------
Define a function that converts the input list into a set to filter duplicates, calculates the sum and count of 
these unique elements, and computes the average while handling potential division by zero scenarios.
"""

def cal_average(arr):
    s = set(arr)
    setsum = sum(s)
    totalnum = len(s)
    if totalnum != 0:
        avg =setsum/totalnum
        return avg   
    else:
        print(f"Sum of all Unique elements is Zero")
        return 0
    

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    n = int(input("Enter How many Unique Numbers average do you want to calculate: "))
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
        result = cal_average(arr)
        print(f"Average : {result}")
        print('\n','*'*30,"Thank You",'*'*30,'\n')