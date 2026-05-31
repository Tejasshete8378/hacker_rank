"""
PROBLEM STATEMENT : String Mutation at a Specific Position
---------------------------------------------------------------------------------------------
Objective:
Modify a given string by replacing a character at a specific index/position with a new character.

Constraint:
- The position index must be a valid integer within the bounds of the string length (0 <= position < len(string)).
- Strings are immutable in Python, so the modification must be done by converting the string into a mutable 
data structure (like a list) and back.

Input:
- A string (s)
- An integer index position (i)
- A single character (c)

Output:
- The modified string with the character at the specified index replaced.

Task:
Convert the input string into a list, replace the element at the specified index with the new character, 
join the list back into a string, and print the updated string wrapped in a user-friendly console interface.

"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    s_new = ''.join(l)
    return s_new

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    s = input("Enter String: ")
    print()
    i = input("Enter Position to Insert: ") 
    print()
    c = input("Enter Character to Insert: ")
    print()
    s_new = mutate_string(s, int(i), c)
    print(f"Modified String: {s_new}")
    print()
    print('*'*30,"Thank You",'*'*30)
    print()