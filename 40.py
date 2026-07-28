if __name__ == '__main__':
    print('\n','*'*30, "Welcome to the Program",'*'*30,'\n')
    a = int(input("Enter First Number: "))
    print()
    b = int(input("Enter Second Number: "))
    print()

    int_div = a//b
    mod_div = a%b
    div_mod = divmod(a,b)

    print(f"Integer Division = {int_div}\n")
    print(f"Modulo Division = {mod_div}\n")
    print(f"Divmod = {div_mod}\n")

    print('\n','*'*30, "Thank You",'*'*30,'\n')