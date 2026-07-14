"""
PROBLEM STATEMENT : Symmetric Difference Calculator
---------------------------------------------------------------------------------------------
Objective:
--------------
To identify and display the symmetric difference between two distinct sets of integers 
provided by the user.

Constraint:
--------------
1. The program must validate that the number of elements entered by the user matches 
   the total count specified for each set.
2. If the input count does not match the total or if the set is empty, the program 
   must terminate with an appropriate error message using sys.exit().
3. The final result must be displayed in ascending order.

Input:
--------------
1. An integer representing the total number of elements in Set1.
2. A sequence of integers separated by spaces for Set1.
3. An integer representing the total number of elements in Set2.
4. A sequence of integers separated by spaces for Set2.

Output:
--------------
The symmetric difference of the two sets (elements that are in either Set1 or Set2, 
but not in both), printed each on a new line in ascending order.

Task:
--------------
Accept two sets of numbers from the user, ensure the input length matches the user's 
declared size, calculate the symmetric difference between them, and print the resulting 
unique elements sorted numerically.
"""

import sys

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')

    #Handling Set1
    set1_total = int(input("Enter Total Number of Elements of Set1: "))
    print()
    data1 = map(int, input("Enter Set1 Elements: ").split())
    listed_data1 = list(data1)
    print()
    if len(listed_data1) < set1_total:
        sys.exit(f"Total Numbers entered is less than {set1_total}\n") 
    elif len(listed_data1) > set1_total:
        sys.exit(f"Total Numbers entered is more than {set1_total}\n")
    elif len(listed_data1) == 0:
        sys.exit(f"Please Enter Set1 Elements\n")
    else:
        set1 = set(listed_data1)

    #Handling Set2
    set2_total = int(input("Enter Total Number of Elements of Set2: "))
    print()
    data2 = map(int, input("Enter Set2 Elements: ").split())
    listed_data2 = list(data2)
    print()
    if len(listed_data2)< set2_total:
        sys.exit(f"Total Numbers entered is less than {set2_total}\n") 
    elif len(listed_data2) > set2_total:
        sys.exit(f"Total Numbers entered is more than {set2_total}\n")
    elif len(listed_data2) == 0:
        sys.exit(f"Please Enter Set2 Elements\n")
    else:
        set2 = set(listed_data2)
    
    #Calculation
    result = set1.symmetric_difference(set2)
    final_result = sorted (result)

    #Output
    print("Symmetrically Different elements are as follows: ")
    for item in final_result:
        print(item)

    print('\n','*'*30,"Thank You",'*'*30,'\n')