import textwrap

def wrap(string, max_width):
    if 0<len(string)<1000 and 0<max_width<len(string):
        result = textwrap.fill(string, max_width)
        return result

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(f"Wrapped Text: \n {result}")
    print('\n','*'*30,"Thank You",'*'*30,'\n')
