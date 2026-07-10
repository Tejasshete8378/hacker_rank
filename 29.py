from collections import namedtuple

if __name__ == '__main__':
    
    s = int(input("Enter Total Number of Students"))
    col_names = input("Enter Coloumn Names").split()
    marks_index = col_names.index('MARKS')
    Student = namedtuple('Student', col_names)

    total_marks = 0
    for i in range (s):
        student = Student(*input("Enter Data").split())
        total_marks = total_marks + int(student.MARKS)

    Average = total_marks/s

    print(f"Average of Marks:{Average:.2f}")
