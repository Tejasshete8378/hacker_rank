"""
PROBLEM STATEMENT : Single Newspaper Subscription Analysis
---------------------------------------------------------------------------------------------
Objective:
--------------
To determine and display the roll numbers of students who are subscribed to exactly one newspaper (either English or French, but not both) and calculate the total count of such students.

Constraint:
--------------
- Roll numbers are input as strings and stored in sets.
- Uses set symmetric difference operation to find elements present in either set but not in both.

Input:
--------------
- Total number of students subscribed to the English newspaper (integer), followed by their respective roll numbers.
- Total number of students subscribed to the French newspaper (integer), followed by their respective roll numbers.

Output:
--------------
- The set of roll numbers belonging to students having a single subscription.
- The total count of students having a single subscription.

Task:
--------------
Write a Python program that accepts roll numbers for English and French newspaper subscribers using sets, computes the symmetric difference to find students with a single subscription, and outputs both the resulting roll numbers and their total count.

"""


if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    total_eng = int(input("Enter total number of Students Subscribed to English Newspaper: "))
    set_eng = set()
    print("Enter Roll Numbers of Students Subscribed to English Newspaper: \n")
    for i in range(total_eng):
        set_eng.add(input(f"Enter Roll Number of Student {i+1}: "))
        print()

    total_french = int(input("Enter Total number of Students Subscribed to French Newspaper: "))
    set_french = set()
    print("Enter Roll Numbers of Students Subscribed to French Newspaper: \n")
    for i in range(total_french):
        set_french.add(input(f"Enter Roll Number of Student {i+1}: "))
        print()

    # ^ for Symmetric_Difference
    single_sub = set_eng^(set_french)
    Total_single_sub = len(single_sub)

    print(f"Roll Numbers of Students having single Subscription are: {single_sub}")
    print(f"Total Number of Students having single Subscription are: {Total_single_sub}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')
    
