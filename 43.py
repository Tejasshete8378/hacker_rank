if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    eng_num = int(input("Enter Number of Students Subscribed to English Newspaper: ").strip())
    print()
    eng_roll = set()
    for i in range(eng_num):
        eng_roll.add(input(f"Enter Roll Number of Studens No. {i+1}: ").strip())
        print()

    french_num = int(input("Enter Number of Students Subscribed to French Newspaper: ").strip())
    print()
    french_roll = set()
    for i in range(french_num):
        french_roll.add(input(f"Enter Roll Number of Studens No. {i+1}: ").strip())
        print()

    unique_roll = eng_roll.difference(french_roll)
    total_unique = len(unique_roll)

    print(f"Unique Roll Numbers are: {unique_roll}\n") 
    print(f"Total Unique Roll Numbers are: {total_unique}")

    print('\n','*'*30,"Thank You",'*'*30,'\n')



