if __name__ == '___main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append[(name, score)]

        unique_score =  sorted(list(set(x[1] for x in records )))

        second_lowest_grade = unique_score[1]

        final_name = sorted(x[0] for x in records if x == second_lowest_grade)
        
        print(final_name)

