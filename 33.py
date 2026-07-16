"""
PROBLEM STATEMENT : Unique Country Stamp Counter 
---------------------------------------------------------------------------------------------
Objective:
--------------
To determine the total number of distinct country names from a collection of inputs provided by the user.

Constraint:
--------------
The count of entries (n) must be an integer, and the program must iterate exactly n times to collect country names[cite: 1].

Input:
--------------
An integer representing the total number of country stamps, followed by n individual lines, each containing a country name[cite: 1].

Output:
--------------
The total count of unique country names provided in the input[cite: 1].

Task:
--------------
Collect a specified number of country names from the user, store them in a data structure that automatically handles uniqueness, and print the final count of distinct entries[cite: 1].
"""

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    n = int(input("Enter total count of Country Names: "))
    print()
    s = set()
    
    for i in range(1,n+1):
        c_name = input(f"Enter Country {i} name: ")
        print()
        s.add(c_name)

    print(f"Total Unique Country Number: {len(s)}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')