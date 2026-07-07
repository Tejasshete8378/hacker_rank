# Defaultdict code

from collections import defaultdict
if __name__ == '__main__':
    n,m = map(int, input().split())
    d = defaultdict(list)
    i = 0
    for i in range(n):
        word = input()
        d[word].append(i+1)
    
    for i in range(m):
        text = input()
        if text in d:
            print(*d[text])
        else:
            print("-1")