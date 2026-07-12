"""
PROBLEM
STATEMENT : Dynamic Student Records Average Calculator 
---------------------------------------------------------------------------------------------
Objective:
--------------
To calculate the average marks of a group of students based on user-defined column headers 
using the 'namedtuple' data structure.

Constraint:
--------------
1. The input must include a column explicitly named 'MARKS'.
2. The number of students and their respective data points must be provided during runtime.
3. The program must handle dynamic column naming and map data to the correct attribute of the namedtuple.

Input:
--------------
1. An integer representing the total number of students.
2. A space-separated string of column names (e.g., "ID NAME MARKS CLASS").
3. For each student, a space-separated string of data corresponding to the column names provided earlier.

Output:
--------------
The calculated average of the 'MARKS' column, formatted to two decimal places.

Task:
--------------
Implement a program that utilizes collections.namedtuple to store student data dynamically based on user input, 
extracts the marks, computes the sum, and outputs the final average.
"""


from collections import namedtuple

if __name__ == '__main__':
    
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    s = int(input("Enter Total Number of Students: "))
    print()
    col_names = [name.upper() for name in input("Enter Column Names: ").split()]
    print()
    
    marks_index = col_names.index('MARKS')
    Student = namedtuple('Student', col_names)
    total_marks = 0
    
    for i in range(s):    
        student = Student(*[item.upper() if i != marks_index else item for i, item in enumerate(input("Enter Data: ").split())])
        print()
        total_marks = total_marks + int(student.MARKS)

    Average = total_marks / s

    print(f"Average of Marks: {Average:.2f}")
    print('\n','*'*30,"Thank You",'*'*30,'\n')