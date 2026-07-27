"""
PROBLEM STATEMENT : Find Students Subscribed to Both Newspapers
---------------------------------------------------------------------------------------------
Objective:
--------------
Determine the total count of students who have subscribed to both English and French newspapers.

Constraint:
--------------
Roll numbers are accepted as string inputs and stored in sets to eliminate duplicates.

Input:
--------------
1. Total number of students subscribed to the English newspaper (integer) and their respective roll numbers.
2. Total number of students subscribed to the French newspaper (integer) and their respective roll numbers.

Output:
--------------
The total count of students whose roll numbers appear in both subscription lists.

Task:
--------------
Accept roll numbers for English and French newspaper subscribers into separate sets, find their intersection, and print the total count of students present in both subscriptions.

"""

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    total_eng = int(input("Enter Total Number of Students subscribed to the English Newspaper: "))
    print()
    print("Enter Roll Numbers of Students subscibed for English Newspaper: \n")

    english = set()
    for i in range(total_eng):
        english.add(input(f"Enter Roll No. of Student {i+1}: "))
        print()

    total_french = int(input("Enter Total Number of Students subscribed to the French Newspaper: "))
    print()
    print("Enter Roll Numbers of Students subscibed for French Newspaper: \n")

    french = set()
    for i in range(total_french):
        french.add(input(f"Enter Roll No. of Student {i+1}: "))
        print()

    result = len(english.intersection(french))

    print(f"Total Number of Students who subscribed to both English and French Newspaper are: {result}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')

