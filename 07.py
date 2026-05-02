if __name__ == '__main__':
    demand = int(input("How many numbers you want to enter: "))
    count = 0
    scores = []
    while count < demand:
        n = int(input(f"Enter Number {count + 1}: "))
        scores.append(n)
        count = count + 1

