"""
PROBLEM
STATEMENT : Word Index Tracking with Defaultdict
---------------------------------------------------------------------------------------------
Objective:
--------------
Create a program that tracks the positions of words from a primary group and checks for their occurrence in a secondary group.

Constraint:
--------------
- The input consists of two integers, 'n' and 'm', followed by 'n' words for the first group and 'm' words for the second group.
- The indices should be 1-based (i.e., the first word is at index 1).
- If a word from the second group is found in the first group, print all its 1-based indices space-separated.
- If a word is not found in the first group, print -1.

Input:
--------------
- Two integers n and m.
- n lines, each containing a word belonging to the first group.
- m lines, each containing a word belonging to the second group to be queried.

Output:
--------------
- For each query word from the second group, output the indices where it appeared in the first group (if present) or -1 (if not present).

Task:
--------------
Implement a dictionary-based lookup system using `defaultdict` to store a list of indices for each word encountered in the first group, then efficiently retrieve these indices for words in the second group.
"""



from collections import defaultdict
if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program","*"*30,'\n')
    n = int(input("Enter Number of First Group words: "))
    print()
    m = int(input("Enter Number of Second Group words: "))
    print()
    
    d = defaultdict(list)
    i = 0
    for i in range(n):
        word = input("Enter First Group words: ")
        print()
        d[word].append(i+1)
        print()

    for i in range(m):
        text = input("Enter Second Group words: ")
        print()
        if text in d:
            print("Index:{}".format(" ".join(map(str, d[text]))))
            print()
        else:
            print("Not Available in First Group of words: -1")
            print()

print('\n','*'*30,"Thank You","*"*30,'\n')