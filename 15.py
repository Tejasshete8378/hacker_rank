"""
PROBLEM STATEMENT : Substring Occurrence Counter
---------------------------------------------------------------------------------------------
Objective:
Find the total number of times a specific substring (sub_text) appears within a given 
string (text), including overlapping occurrences.

Constraint:
- The input strings should have their leading and trailing whitespaces removed before processing.
- The search should check all possible sequential windows of the text that match the length of the substring.

Input:
- text (string): The main body of text to search within.
- sub_text (string): The target substring to find.

Output:
- An integer representing the total count of the substring's occurrences in the text.

Task:
Implement a function that uses a sliding window approach to scan the main text, 
compare slices against the target substring, and return the final frequency count.
"""

def find_count(text, sub_text):
    len_sub = len(sub_text)
    count = 0
    for i in range(len(text) - len_sub + 1):
        if text[i:i + len_sub] == sub_text:
            count = count + 1
    return count

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    text = input("Enter Text: ").strip()
    print()
    sub_text = input("Enter Sub Text: ").strip()
    print()
    result = find_count(text, sub_text)
    print(f"Count = {result}")
    print()
    print('*'*30,"Thank You",'*'*30)
    print()