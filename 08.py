"""
PROBLEM STATEMENT : Nested Lists and Second Lowest Grade
---------------------------------------------------------------------------------------------
Objective:
Store student names and their corresponding grades in a nested list and identify the students 
who have the second-lowest grade.

Constraint:
- The program requires at least two unique grade values to identify a second-lowest score.
- If multiple students share the second-lowest grade, their names must be displayed 
  in alphabetical order.

Input:
1. An integer representing the total number of students.
2. For each student, a string representing the name and a float representing the score.

Output:
A list of names and scores of the students who achieved the second-lowest grade, 
sorted alphabetically by name.

Task:
Collect student data into a nested list, determine the unique scores to find the second 
position from the bottom, and filter the students who match that specific score.
"""

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    records = []
    user_input = int(input("Enter how many students data you want to enter: "))
    print()
    for student in range(user_input):
        name = input("Enter Name: ")
        print()
        score = float(input("Enter Score: "))
        print()
        records.append([name, score])

    print()
    print(f"Total List: {records}")
    print()
    unique_score =  sorted(list(set(x[1] for x in records )))

    if len(unique_score)<2:
        print("Not enough Unique Scores to find Runner-Up")
    else:
        second_lowest_grade = unique_score[-2]

    final_name = sorted(x[0] for x in records if x[1] == second_lowest_grade)
        
    print("Second Runner-Up details are as follows: ")
    print()
    for student in final_name:
        print(f"Student Name: {student} and Student Score: {second_lowest_grade} ")
print()
print('*'*30,"Thank You",'*'*30)
print()

