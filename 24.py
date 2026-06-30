from itertools import permutations

if __name__ == '__main__':

    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    text = input("Enter Text: ")
    print()
    iterable = int(input("Enter Iterable: "))
    print()

    sorted_text = "".join(sorted(text))

    perms = list(permutations(sorted_text, iterable))

    print("Lexicographic Permutations are as follows:")
    for i in perms:
        result = "".join(i)
        print(result)

    print('\n','*'*30,"Thank You",'*'*30,'\n')