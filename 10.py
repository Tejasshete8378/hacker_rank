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
    N = int(input())
    res_list =[]
    for i in range(N):
        command = input().split()
        
        action = command[0]
        
        if action == 'Insert':
            res_list.insert(int(command[1]),int(command[2]))
        elif action == 'print':
            print(res_list)
        elif action == 'remove':
            res_list.remove(int(command[1]))
        elif action == 'append':
            res_list.append(int(command[1]))
        elif action == 'sort':
            res_list.sort()
        elif action == 'pop':
            res_list.pop()
        elif action == 'reverse':
            res_list.reverse()