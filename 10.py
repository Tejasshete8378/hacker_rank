'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands 
where each command will be of the 7 types listed above. Iterate through each command 
in order and perform the corresponding operation on your list.'''





if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    
    N = int(input("Enter how many values you want to enter: "))
    print()
    res_list =[]
    
    for i in range(N):
        action = input("Enter Name of Operation ").lower()
        print()
        
        if action == 'insert':
            insert_index = int(input("Enter Index: "))
            insert_value = int(input("Enter Value: "))
            res_list.insert(insert_index,insert_value)
        elif action == 'print':
            print(res_list)
        elif action == 'remove':
            remove_num = int(input("Enter Number to be Removed: "))
            if remove_num in res_list:
                res_list.remove(remove_num)
            else:
                print("Entered Numbered does not belong to the List")
        elif action == 'append':
            append_num = int(input("Enter Number to Append: "))
            res_list.append(append_num)
        elif action == 'sort':
            res_list.sort()
        elif action == 'pop':
            if res_list:  # It will check that the list is not empty
                res_list.pop()
            else:
                print("List is Empty")
        elif action == 'reverse':
            res_list.reverse()
        else:
            print("Please enter Valid Input")
            print()
    print(f"Final List: {res_list}")
print('*'*30,"Thank You",'*'*30)
print()