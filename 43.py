"""
PROBLEM STATEMENT : Students Subscribed to English Newspaper Only
---------------------------------------------------------------------------------------------
Objective:
--------------
To find and display the roll numbers and total count of students who are subscribed exclusively to the English newspaper and 
not to the French newspaper.

Constraint:
--------------
- Roll numbers are entered as strings and stored using sets to automatically handle uniqueness.
- Input counts for both subscriptions must be valid integers.

Input:
--------------
- An integer representing the number of students subscribed to the English newspaper.
- A sequence of student roll numbers subscribed to the English newspaper.
- An integer representing the number of students subscribed to the French newspaper.
- A sequence of student roll numbers subscribed to the French newspaper.

Output:
--------------
- The roll numbers of students subscribed to the English newspaper only.
- The total count of students subscribed to the English newspaper only.

Task:
--------------
Read the roll numbers of students subscribed to English and French newspapers, determine those who take 
only the English newspaper using set difference, and output their roll numbers along with the total count.
"""


if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    eng_num = int(input("Enter Number of Students Subscribed to English Newspaper: ").strip())
    print()
    eng_roll = set()
    for i in range(eng_num):
        eng_roll.add(input(f"Enter Roll Number of Studens No. {i+1}: ").strip())
        print()

    french_num = int(input("Enter Number of Students Subscribed to French Newspaper: ").strip())
    print()
    french_roll = set()
    for i in range(french_num):
        french_roll.add(input(f"Enter Roll Number of Studens No. {i+1}: ").strip())
        print()

    only_eng_roll = eng_roll.difference(french_roll)
    total_eng_roll = len(only_eng_roll)

    print(f"Roll Numbers of Students Subscribed to English Newspaper only are: {only_eng_roll}\n") 
    print(f"Total Number of Students Subscribed to English Newspaper only are: {total_eng_roll}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')



