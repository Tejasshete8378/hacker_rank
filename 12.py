if __name__ == '__main__':
    n = int(input("Enter Number of Integers: "))
    i = 0
    name_list = []

    for i in range(n):
        l = map(int, input(f"Enter {i+1} integer: ").split())
        name_list.append(l)
    
    t = tuple(l)
    print(hash(t))
