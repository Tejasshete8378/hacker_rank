"""
itertools.product()
--------------------

Task
---------------
You are given a two lists A and B. Your task is to compute their cartesian product AXB.

Example
---------------
A = [1, 2]
B = [3, 4]

AxB = {(1, 3), (1, 4), (2, 3), (2, 4)}
Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format
---------------
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

Constraints
---------------
0 < A < 30
0 < B < 30

Output Format
---------------
Output the space separated tuples of the cartesian product.

Sample Input
---------------
1 2
3 4

Sample Output
---------------
(1, 3) (1, 4) (2, 3) (2, 4)
"""


from itertools import product

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    A = list(map(int, input("Enter First List Elements: ").split()))
    print()
    B = list(map(int, input("Enter Second List Elements: ").split()))
    print()
    
    product_list = list(product(A,B))
    formatted_output = " ".join(map(str, product_list))
    
    print(f"Cartesian Product = {formatted_output}")
    
    print('\n','*'*30,"Thank You",'*'*30,'\n')

    