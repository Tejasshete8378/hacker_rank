def solve(s):
    words = s.split(" ")
    capitalize_word = [word.capitalize() if word else word for word in words]
    return " ".join(capitalize_word)

if __name__ == '__main__':
    print('\n',"*"*30,"Welcome to the Program","*"*30,'\n')
    text = input("Enter Text: ")
    print()
    result = solve(text)
    print(f"Capitalized Text: {result}")
    print('\n',"*"*30,"Thank You","*"*30,'\n')