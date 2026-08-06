# Set Mutations Problem on Hackerrank

"""
PROBLEM STATEMENT : Set Mutations Problem Implementation
---------------------------------------------------------------------------------------------
Objective:
--------------
To dynamically process a starting set of integers and apply various set mutation operations 
(update, intersection_update, difference_update, symmetric_difference_update) based on multiple 
subsequent inputs, and finally compute the sum of the remaining elements in the set.

Constraint:
--------------
- The input operations must be one of the four valid mutation commands.
- Elements within sets must be handled as integers to allow proper arithmetic operations (like sum).

Input:
--------------
- Total number of elements in the first set.
- Space-separated elements of the first set (Set A).
- Number of other sets / operations to follow.
- For each operation:
  - Operation name (string).
  - Length of the other set.
  - Space-separated elements of the other set.

Output:
--------------
- The current state of Set A after each operation step.
- The total sum of all elements remaining in Set A after all operations have completed.

Task:
--------------
Accept dynamic user input for an initial set of numbers and a series of mutation operations. 
Execute each requested set mutation method iteratively using conditional control flow, 
and output the final sum of the elements in Set A.

"""


if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    total_a = int(input("Enter Total Number of Elements of First Set: "))
    print()
    set_a = set(map(int, input("Enter space separated Elements of Set A: ").split()))
    print()
    other_set_num = int(input("Enter Number of Other Sets: "))
    print()

    for i in range(1, other_set_num+1):
        op_name = input("Enter Operation Name: ")
        print()
        other_set_len = int(input("Enter Length of Other Set: "))
        print()
        other_set= set(map(int, input("Enter space separated Elements of Other Set: ").split()))
        print()

        if op_name == 'intersection_update': 
            set_a.intersection_update(other_set)
        elif op_name == 'update':
            set_a.update(other_set)
        elif op_name == 'symmetric_difference_update':
            set_a.symmetric_difference_update(other_set)
        elif op_name == 'difference_update':
            set_a.difference_update(other_set)

        print(f"Current Set: {set_a} \n")

    print(f"The Sum of all elements of Set A: {sum(set_a)}\n")

    print('\n','*'*30,"Thank You",'*'*30,'\n')