"""
PROBLEM STATEMENT : Multi-Variable Coordinate Permutations
---------------------------------------------------------------------------------------------
Objective:
Generate a comprehensive list of all possible 3D coordinate triplets [i, j, k] 
within specified boundaries, excluding those whose sum matches a given constraint.

Constraint:
0 <= i <= x, 0 <= j <= y, 0 <= k <= z, and (i + j + k) != n

Input:
Four integers representing the maximum limits for x, y, and z, and a sum 
constraint value n.

Output:
A list of coordinate lists [[i, j, k], ...] that satisfy the exclusion logic.

Task:
Capture four user inputs and call a filtering function to perform a nested 
iteration across all three dimensions, returning only the coordinates where 
 the sum of the indices is not equal to n.
"""

def get_filtered_coordinates(x,y,z,n):
    return [[i,j,k] 
            for i in range(x+1) 
            for j in range(y+1) 
            for k in range(z+1) 
            if i+j+k != n ]
    
print('*'*30,"Welcome to the Program",'*'*30)
print()
if __name__ == '__main__':
    x = int(input("Enter First Coordinate limit(x): "))
    print()
    y = int(input("Enter Second Coordinate limit(y): "))
    print()
    z = int(input("Enter Third Coordinate limit(z): "))
    print()
    n = int(input("Enter Sum Constraint (n): "))
    print()
    result = get_filtered_coordinates(x,y,z,n)
    print(f"Filtered Coordinates: {result}")

print()
print('*'*30,"Thank You",'*'*30)


