if __name__ == '__main__':
    records = []
    user_input = int(input("Enter how many students data you want to enter: "))
    for student in range(user_input):
        name = input("Enter Name: ")
        score = float(input("Enter Score: "))
        records.append([name, score])

    print(f"Total List: {records}")

    unique_score =  sorted(list(set(x[1] for x in records )))

    if len(unique_score)<2:
        print("Not enough Unique Scores to find Runner-Up")
    else:
        second_lowest_grade = unique_score[-2]

    final_name = sorted(x[0] for x in records if x[1] == second_lowest_grade)
        
    print("Runner-Up details are as follows: ")

    for student in final_name:
        print(f"Student Name: {student[0]} and Student Score: {student[1]} ")

