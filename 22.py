import string

chars = string.ascii_lowercase

lines = []

def print_rangoli(size):
    for i in range(size):

        s = '-'.join(chars[size-1:i:-1] + chars[i:size])
        lines.append(s.center(4*size - 3, '-'))

    rangoli = '\n'.join(lines[size::-1] + lines[1:size])
    print(rangoli)

if __name__ == '__main__':
    n = int(input("Enter Size: "))
    print_rangoli(n)