"""
PROBLEM STATEMENT : Dynamic List Operations Menu
---------------------------------------------------------------------------------------------
Objective:
Develop an interactive command-line application that allows a user to perform a 
specified number of list manipulation operations on a collection of integers.

Constraint:
- The program must execute exactly N times as defined by the initial user input.
- Input strings for operations must be case-insensitive and handle leading/trailing spaces.
- Must include a safety check to prevent errors when attempting to pop from an empty list.
- All numerical inputs (indices and values) must be handled as integers.

Input:
- An integer N representing the total number of operations to be performed.
- A string representing the action name: 'insert', 'print', 'remove', 'append', 
  'sort', 'pop', or 'reverse'.
- Subsequent integers for specific operations (e.g., index and value for 'insert').

Output:
- A welcoming and closing header.
- A menu showing the list of available operations for every iteration.
- The state of the list after each command is executed.
- Error messages for invalid commands or invalid 'remove' requests.

Task:
Write a Python script that initializes an empty list and uses a 'for' loop to 
repeatedly prompt the user for commands. Use conditional logic (if-elif-else) 
to map user inputs to built-in list methods, ensuring the current list is 
displayed to the user after every modification.
"""

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    
    N = int(input("Enter how many values you want to enter: "))
    print()
    res_list =[]
    
    for i in range(N):
        print("List of Operations:\n1) Insert\n2) Print\n3) Remove\n4) Append\n5) Sort\n6) Pop\n7) Reverse")
        print()
        action = input("Enter Name of Operation: ").lower().strip()
        print()
        
        if action == 'insert':
            insert_index = int(input("Enter Index: "))
            print()
            insert_value = int(input("Enter Value: "))
            print()
            res_list.insert(insert_index,insert_value)
            print(f"Current List: {res_list}")
            print()

        elif action == 'print':
            print(f"Current List: {res_list}")
            print()
        
        elif action == 'remove':
            remove_num = int(input("Enter Number to be Removed: "))
            print()
            if remove_num in res_list:
                res_list.remove(remove_num)
            else:
                print(f"{remove_num} does not belong to the List")
                print()
            print(f"Current List: {res_list}")
            print()
        
        elif action == 'append':
            append_num = int(input("Enter Number to Append: "))
            print()
            res_list.append(append_num)
            print(f"Current List: {res_list}")
            print()
        
        elif action == 'sort':
            res_list.sort()
            print(f"Current List: {res_list}")
            print()
        
        elif action == 'pop':
            if len(res_list)>0:  # It will check that the list is not empty
                res_list.pop()
            
            else:
                print("List is Empty")
                print()
            print(f"Current List: {res_list}")
            print()
        
        elif action == 'reverse':
            res_list.reverse()
            print(f"Current List: {res_list}")
            print()
        
        else:
            print("Invalid Input. Please enter Valid Input")
            print()

    print(f"Final List: {res_list}")
    print()
    print('*'*30,"Thank You",'*'*30)
    print()