'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2<=n<=10
-100<=A[i]<=100 ==> This means that every element of an array should be between -100 and 100

'''

if __name__ == '__main__':
    demand = int(input("How many scores you want to enter: "))
    count = 0
    scores = []

    if 2<=demand<=10:
        while count < demand:
            n = int(input(f"Enter Number {count + 1}: "))
            if -100<=n<=100:
                scores.append(n)
                count = count + 1
            else:
                print("Score is out of Range please enter Score between -100 and 100")

    if len(scores)>=2:
        unique_scores = sorted(list(set(scores)))
        if len(unique_scores)>=2:
            runner_up = unique_scores[-2]
            print(f"Runner_Up Score: {runner_up}")
    else:
        print("Atleast Two Scores are needed to find Runner-Up")




