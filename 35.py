"""
PROBLEM STATEMENT : Robust Set Operations Manager
---------------------------------------------------------------------------------------------
Objective:
--------------
To develop an interactive Python program that manages a set of integers and performs 
mutating operations (remove, discard, pop) while handling potential runtime errors 
gracefully, culminating in a final summation of the remaining elements.

Constraint:
--------------
- The program must handle 'remove', 'discard', and 'pop' operations.
- 'remove' must be handled to avoid KeyError if the element is absent.
- 'pop' must be handled to avoid KeyError if the set is empty.
- The output should provide visual feedback of the set after each operation.

Input:
--------------
- An integer representing the total number of elements.
- A space-separated list of integers to initialize the set.
- An integer representing the total number of commands.
- A sequence of commands (e.g., 'remove 9', 'pop', 'discard 8').

Output:
--------------
- Display the current state of the set after each operation.
- The final sum of all elements remaining in the set.

Task:
--------------
Implement a loop-based control flow that parses user-provided set commands, 
safely executes the requested set mutations using try-except blocks, and 
tracks the internal state of the set for display purposes.
"""

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    n = int(input("Enter Total Number of Elements in Set: "))
    print()
    set_ele = map(int, input("Enter Elements of Set separated by spaces: ").split())
    print()
    s = set(set_ele)
    nc = int(input("Enter Number of Commands: "))
    print()

    for i in range(1, nc+1):
        x = input(f"Enter Command No. {i}: ").split()
        print()
        if x[0] == 'remove':
            y = int(x[1])
            try:
                s.remove(y)
            except KeyError:
                pass
            print(f"Current Set = {s}")
            print()
        
        elif x[0] == 'pop':
            try:
                s.pop()
            except KeyError:
                pass
            print(f"Current Set = {s}")
            print()
        
        elif x[0] == 'discard':
            z = int(x[1])
            s.discard(z)
            print(f"Current Set = {s}")
            print()

    print(f"Sum of Elements of Set = {sum(s)}")
    print('\n','*'*30,"Thank You",'*'*30,'\n')