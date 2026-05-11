'''
PROBLEM STATEMENT : Student Grade Average Calculator
---------------------------------------------------------------------------------------------
Objective:
Create a script to store student names and their respective marks in a dictionary and 
calculate the average score for a specific student.

Constraint:
1. The number of students (n) must be an integer.
2. Each student entry must contain a name followed by a sequence of scores.
3. The average score must be displayed with exactly two decimal places.

Input:
1. An integer representing the total number of students.
2. For each student, a string containing the Name and multiple scores separated by spaces.
3. A query string representing the name of the student to search for.

Output:
1. A welcome and exit banner.
2. The calculated average of the queried student if they exist in the records.
3. An error message if the student name is not found.

Task:
Read student data into a dictionary, look up a specific student's scores, compute the 
arithmetic mean, and format the result to 2 decimal places.
'''

if __name__ == '__main__':
    print()
    print('*'*30,"Welcom to the Program",'*'*30)
    print()
    
    n = int(input("How many Students records due you want to enter: "))
    print()
    student_marks = {}
    
    for _ in range(n):
        name, *line = input("Enter Name and Scores separated by Spaces: ").split()
        print()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input("Enter the Name of Student to display Average: ")
    print()
    
    if query_name in student_marks:
        marks = student_marks[query_name]
        avg = sum(marks)/len(marks)
        print(f"Average = {avg:.2f}")
        print()
    else:
        print(f"Student {query_name} not found")
        print()
    print('*'*30,"Thank You",'*'*30)
    print()