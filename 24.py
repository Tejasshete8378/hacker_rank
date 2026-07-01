"""
itertools.permutations()
---------------
Description
---------------
itertools.permutations(iterable[, r])
This tool returns successive r length permutations of elements in an iterable.[cite: 1]

Key Rules
---------------
* If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.[cite: 1]
* Permutations are printed in a lexicographic sorted order.[cite: 1]
* If the input iterable is sorted, the permutation tuples will be produced in a sorted order.[cite: 1]

Sample Code
---------------
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>>
>>>>>> print list (permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2')
, ('2', '1', '3'), ('2', '3', '1'), ('3', '1',
'2'), ('3', '2', '1')]
>>>
>>>> print list (permutations (['1', '2','3'1,2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>>> print list (permutations('abc', 3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a',
'b'), ('c', 'b', 'a')][cite: 1]

Task
---------------
You are given a string S.[cite: 1]
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.[cite: 1]

Input Format
---------------
A single line containing the space separated string S and the integer value k.[cite: 1]

Constraints
---------------
0 < k <= len(S)[cite: 1]
The string contains only UPPERCASE characters.[cite: 1]

Output Format
---------------
Print the permutations of the string S on separate lines.[cite: 1]

Sample Input
---------------
HACK 2[cite: 1]

Sample Output
---------------
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH[cite: 1]

Explanation
---------------
All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.[cite: 1]
"""

from itertools import permutations

if __name__ == '__main__':

    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    text = input("Enter Text: ")
    print()
    iterable = int(input("Enter Iterable: "))
    print()

    sorted_text = "".join(sorted(text))

    perms = list(permutations(sorted_text, iterable))

    print("Lexicographic Permutations are as follows:")
    for i in perms:
        result = "".join(i)
        print(result)

    print('\n','*'*30,"Thank You",'*'*30,'\n')