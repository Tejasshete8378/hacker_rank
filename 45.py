if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    total_eng = int(input("Enter total number of Students Subscribed to English Newspaper: "))
    set_eng = set()
    print("Enter Roll Numbers of Students Subscribed to English Newspaper: \n")
    for i in range(total_eng):
        set_eng.add(input(f"Enter Roll Number of Students {i+1}: "))
        print()

    total_french = int(input("Enter Total number of Students Subscribed to French Newspaper: "))
    set_french = set()
    print("Enter Roll Numbers of Students Subscribed to French Newspaper: \n")
    for i in range(total_french):
        set_french.add(input(f"Enter Roll Number of Students {i+1}: "))
        print()

    single_sub = set_eng.symmetric_difference(set_french)
    Total_single_sub = len(single_sub)

    print(f"Roll Numbers of Students having single Subscription are: {single_sub}")
    print(f"Total Number of Students having single Subscription are: {Total_single_sub}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')
    
