if __name__ == '__main__':

    data=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
        
        data.sort(key = lambda x: x[1], reverse = True)