"""
PROBLEM STATEMENT : Newspaper Subscription Union Manager 
---------------------------------------------------------------------------------------------
Objective:
--------------
To determine and display the total number and sorted list of unique students who have subscribed 
to at least one newspaper (either English or French) using Python set operations.

Constraint:
--------------
- Student names are read as space-separated strings and converted into sets for set union operations.
- Subscription counts provided as inputs should match the actual number of names entered.

Input:
--------------
- An integer `s1` followed by a space-separated string of student names subscribed to the 
English newspaper.
- An integer `s2` followed by a space-separated string of student names subscribed to the 
French newspaper.

Output:
--------------
- The total count of unique students subscribed to at least one newspaper.
- A numbered, alphabetically sorted list of all unique student names.

Task:
--------------
Write a Python program that takes subscription inputs for English and French newspapers, computes 
their union to find unique subscribers, and prints out the sorted roster with sequential 
enumeration.

"""


if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    s1 = int(input("Enter total number of Students subscibed to English Newspaper: "))
    print()
    english = input("Enter Name of Students subscribed to English Newspaper: ").split() 
    set_english = set(english)
    print()

    s2 = int(input("Enter total number of Students subscibed to French Newspaper: "))
    print()
    french = input("Enter Name of Students subscribed to French Newspaper: ").split()
    set_french = set(french)
    print()

    unique = set_english.union(set_french)
    num_unique = len(unique)

    print(f"Total Number of Students Subscribed to atleast One Newspaper: {num_unique}\n")
    print("Name of Student Subscribed to atleast One Newspaper are as follows:\n")
    for index, name in enumerate(sorted(unique), start = 1):
        print(f"{index}: {name}")
    
    print('\n','*'*30,"Thank You",'*'*30,'\n')
    