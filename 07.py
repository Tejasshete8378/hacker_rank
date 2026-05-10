"""
PROBLEM STATEMENT : Find the Runner-Up Score
---------------------------------------------------------------------------------------------
Objective:
Identify the second-highest unique value from a given list of integer scores.

Constraint:
- The number of scores (n) must be between 2 and 10, inclusive.
- Each individual score must be between -100 and 100, inclusive.

Input:
1. An integer representing the total count of scores to be entered.
2. Individual integers for each score.

Output:
A single integer representing the runner-up score, or an error message if 
constraints are not met.

Task:
Collect a specific number of integer scores from the user, ensure they fall within 
the valid range, remove duplicates, and display the second-largest value.
"""


print()
print('*'*30,"Welcome to the Program",'*'*30)
print()
if __name__ == '__main__':
    demand = int(input("How many scores you want to enter: "))
    print()
    count = 0
    scores = []

    if 2<=demand<=10:
        while count < demand:
            n = int(input(f"Enter Number {count + 1}: "))
            print()
            if -100<=n<=100:
                scores.append(n)
                count = count + 1
            else:
                print("Score is out of Range please enter Score between -100 and 100")
                print()

    if len(scores)>=2:
        unique_scores = sorted(list(set(scores)))
        runner_up = unique_scores[-2]
        print(f"Runner_Up Score: {runner_up}")
        print()
    else:
        print("Atleast Two Scores are needed to find Runner-Up")
        print()

    print('*'*30,"Thank You",'*'*30)
    print()




