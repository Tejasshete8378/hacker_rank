'''
PROBLEM STATEMENT:
Write a Python program that accepts student names and their corresponding 
scores. The program must:
1. Store the data in a nested list format.
2. Identify the second-highest unique score (Runner-Up).
3. Handle cases where there aren't enough unique scores to find a runner-up.
4. Print the names of all students who achieved that specific runner-up score 
   in alphabetical order.
5. Maintain a clean UI using spacing and separators.

INPUT:
- Integer: Number of students.
- String: Name of each student.
- Float: Score of each student.

OUTPUT:
- A nested list of all records.
- Name(s) and Score of the second-highest performer(s).
'''

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

