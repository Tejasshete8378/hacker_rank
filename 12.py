"""
PROBLEM STATEMENT : Dynamic Tuple Creation and Hash Value Generation 
---------------------------------------------------------------------------------------------
Objective:
Accept a dynamic list of integers from the user, convert the list into an immutable tuple, and compute its built-in hash value.

Constraint:
- The number of elements (n) and the elements themselves must be valid integers.
- Built-in functions should be used for type conversion and hashing.

Input:
- An integer 'n' representing the count of total numbers.
- 'n' sequential integers entered by the user one by one.

Output:
- A printed welcome and farewell banner.
- A displayed tuple containing all the entered integers.
- The computed integer hash value of the final tuple.

Task:
Read 'n' integers from the user, store them in a list, convert that list into a tuple, and print both the tuple and its corresponding hash value with clean formatting.
"""


if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    n = int(input("Enter Number of Integers: "))
    print()
    numbers_list = []

    for i in range(n):
        val = int(input(f"Enter Integer {i+1}: "))
        print()
        numbers_list.append(val)
    
    t = tuple(numbers_list)

    print(f"Values you entered: {t}")
    print()
    print(f"Hash Value of Total Values you entered: {hash(t)}")
    print()
    print('*'*30,"Thank You",'*'*30)
    print()