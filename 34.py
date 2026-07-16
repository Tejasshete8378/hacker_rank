"""
PROBLEM STATEMENT: Lexicographic Combinations with Replacement
---------------------------------------------------------------------------------------------
Objective:
Generate all possible combinations of a given length 'n' from a provided string 's', 
allowing for replacement of elements, and output them in lexicographic order.

Constraint:
- The input string consists of characters that must be sorted lexicographically 
  before generating combinations.
- Combinations are generated with replacement (an element can be chosen more than once).
- The output should display each combination on a new line.

Input:
- A string 's' representing the pool of characters.
- An integer 'n' representing the length of the combinations to be generated.

Output:
- A list of all unique combinations of length 'n', each printed as a joined string 
  on a new line.

Task:
- Take a string and an integer as input. Sort the string. Use the itertools library 
  to generate combinations with replacement of length 'n'. Join the resulting 
  tuples into strings and display them sequentially.
"""

from itertools import combinations_with_replacement

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    s = input("Enter String: ")
    print()
    new_s = sorted(s)
    n = int(input("Enter Iterable: " ))
    print()

    iterated_data = combinations_with_replacement(new_s, n)

    print("Iterated Data is as Follows: ",'\n')
    for i in iterated_data:
        result = "".join(i)
        print(result)

    print('\n','*'*30,"Thank You",'*'*30,'\n')
