"""
PROBLEM STATEMENT: 3D Grid Coordinate Filtering
-----------------------------------------------
Objective:
Given dimensions x, y, and z, generate all possible coordinate triplets 
(i, j, k) such that 0 <= i <= x, 0 <= j <= y, and 0 <= k <= z.

Constraint:
Filter the generated list to exclude any triplet where the sum of its 
components equals a target integer n (i + j + k != n).

Task:
Generate a list of valid coordinates using list comprehensions.
"""

def get_filtered_coordinates(x,y,z,n):
    return [[i,j,k] 
            for i in range(x+1) 
            for j in range(y+1) 
            for k in range(z+1) 
            if i+j+k != n ]
    

if __name__ == '__main__':
    x = int(input("Enter First Coordinate limit(x): "))
    y = int(input("Enter Second Coordinate limit(y): "))
    z = int(input("Enter Third Coordinate limit(z): "))
    n = int(input("Enter Sum Constraint (n): "))
    
    result = get_filtered_coordinates(x,y,z,n)
    print(result)


