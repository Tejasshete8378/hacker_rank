"""
PROBLEM STATEMENT : Dynamic Deque Method Execution Manager 
---------------------------------------------------------------------------------------------
Objective:
--------------
To build an interactive command-line utility that allows users to perform various standard 
deque operations dynamically by entering method names and arguments at runtime.

Constraint:
--------------
- The entered command must match an existing valid attribute or method of collections.deque.
- Operation arguments should be correctly parsed into integers when applicable, falling back
safely to strings.

Input:
--------------
- An integer `n` denoting the total count of operations to execute.
- `n` successive lines of user input representing the command name and optional arguments 
(e.g., `append 10`).

Output:
--------------
- Real-time feedback showing method return values (if any), the updated state of the deque 
after each command, and the final collection state.

Task:
--------------
Write a Python script that initializes an empty deque, accepts `n` dynamic method commands from 
the user, validates them using reflection, executes the methods with parsed arguments, and 
displays the step-by-step progress along with error handling.

"""


from collections import deque

if __name__ == '__main__':

    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    d = deque()

    try:
        n = int(input("Enter Total Number of Operations: "))
        print()
    except ValueError:
        print("Invalid Input! Please Enter an Integer \n")
        exit()

    for i in range(n):
        user_input = input(f"Enter Operation {i+1} Name: ").strip().split()
        print()
        if not user_input:
            continue

        cmd = user_input[0]
        # Check if the method exists on the Deque object
        if not hasattr(d, cmd):
            print(f"Error: {cmd} is not a Valid Deque method.\n")
            continue

        try:
            if len(user_input) > 1:
                #Attempt to convert to int, fallback to string if needed
                val = user_input[1]
                try:
                    val = int(val)
                except ValueError:
                    pass

                result = getattr(d, cmd)(val)
            else:
                result = getattr(d, cmd)()
                # Print if a method returns a value (like pop or popleft)
                if result is not None:
                    print(f"Result = {result}\n")

            print(f"Current Deque: {d}\n")

        except Exception as e:
            print(f"Error executing command: {e}\n")

    print(f"Final Elements of Deque: {d}")
    print('\n','*'*30,"Thank You",'*'*30,'\n')




        
   
