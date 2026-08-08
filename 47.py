"""
PROBLEM STATEMENT : The Captain's Room Challenge
---------------------------------------------------------------------------------------------
Story:
--------
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. 
The list consists of the room numbers for all of the tourists. 
The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Input Format:
----------------
The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.

Objective:
--------------
Find and isolate the single unique room number (belonging to the Captain) from a mixed list of room numbers 
where all other family rooms appear in groups of a fixed size.

Constraint:
--------------
- The group size is an integer representing how many times regular family room numbers appear in the list.
- The Captain's room appears exactly 1 time.
- Inputs are provided via standard input (stdin) as size and an unordered space-separated list of room numbers.

Input:
--------------
- First line: An integer representing the group size.
- Second line: A space-separated list of integers representing all room numbers.

Output:
--------------
- A single integer representing the Captain's room number.

Task:
--------------
Implement an efficient algorithm using sets and mathematical sum manipulation to eliminate duplicate family room entries, 
calculate the difference between the scaled unique sum and the actual list sum, and isolate the Captain's room number using integer division.

"""



if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    size = int(input("Enter Size of Each Group: "))
    print()
    room_no = list(map(int, input("Enter space separated Unordered elements of Room No. List: ").split()))
    print()
    unique_set = set(room_no)

    duplicate_sum = sum(room_no)
    unique_sum = sum(unique_set) 

    unique_total = unique_sum*size

    difference = unique_total - duplicate_sum

    captains_room = difference/(size-1)

    print(f"Captain's Room No. = {captains_room}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')