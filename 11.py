def swap_case(s):
    if 0<len(s)<=1000:
        new_output = s.swapcase()
    return new_output

if __name__ == '__main__':
    print()
    print('*'*30,"Welcome to the Program",'*'*30)
    print()
    
    s = input("Enter String: ")
    print()
    result = swap_case(s)
    print(f"Swapped String: {result}")
    
    print()
    print('*'*30,"Thank You",'*'*30)
    print()