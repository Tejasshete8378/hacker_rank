"""
PROBLEM STATEMENT : HackerRank Logo Generator
---------------------------------------------------------------------------------------------
Objective:
Create a text-based ASCII art representation of the HackerRank 'H' logo using a specified 
character ('H') and a user-defined thickness.

Constraint:
- The thickness must be an odd integer (e.g., 3, 5, 7).

Input:
- A single odd integer representing the thickness of the logo.

Output:
- The printed ASCII art of the HackerRank logo scaled to the given thickness.

Task:
Read an odd integer input and use string alignment methods (ljust, rjust, center) 
along with loops to print the five distinct sections of the logo: the top cone, 
top pillars, middle belt, bottom pillars, and bottom cone.
"""
if __name__ == '__main__':

    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')

    thickness = int(input("Enter an Odd Number: ")) #This must be an odd number
    print()
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillers
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

    print('\n','*'*30,"Thank You",'*'*30,'\n')

    