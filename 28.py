"""
PROBLEM STATEMENT: Calendar Day Finder
---------------------------------------------------------------------------------------------
Objective:
Create an interactive program that determines the day of the week for any given date.

Constraint:
- The input must be provided in three separate steps: Day, Month, and Year as integers.
- The output must display the full name of the day in uppercase.
- You must use the built-in 'calendar' module.

Input:
- An integer for the day (1-31).
- An integer for the month (1-12).
- An integer for the year (e.g., 2026).

Output:
- A formatted string displaying the corresponding day of the week (e.g., MONDAY).

Task:
Write a program that prompts the user for day, month, and year inputs, calculates the corresponding day of the week using the calendar module, and prints the result in a clean, user-friendly format.
"""

import calendar

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    print("Enter the Date of which you day you want to find as follow: ")
    print()
    day = int(input("Enter Day: "))
    print()
    month = int(input("Enter Month: "))
    print()
    year = int(input("Enter Year: "))
    print()

    day_list = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    print(f"Day = {day_list[calendar.weekday(year, month, day)]}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')

