"""
PROBLEM STATEMENT : Itertools Combinations Generator
---------------------------------------------------------------------------------------------
Objective:
--------------
Generate and display all possible combinations of a given string up to a specified length k in lexicographic order.

Constraint:
--------------
0 < k <= len(S)
The string S contains only UPPERCASE characters.

Input:
--------------
A single line containing the string S and an integer value k separated by a space.

Output:
--------------
Print all different combinations of string S on separate lines, sorted lexicographically.

Task:
--------------
The program must accept a string and an integer k, sort the string, and then iterate through all combination sizes 
from 1 to k to print every possible combination found.
"""

from itertools import combinations

if __name__ == '__main__':

    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    s = input("Enter String: ")
    print()
    new_s = sorted(s)
    k = int(input("Enter Size: "))
    print()

    print("Result is as Follows: ")
    for i in range(1, k+1):
        final = combinations(new_s, i)
        for j in final:
            result = "".join(j)
            print(result)
            
    print('\n','*'*30,"Thank You",'*'*30,'\n')