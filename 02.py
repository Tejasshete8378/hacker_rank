'''
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

constraints:
1<=a<=10**10
1<=b<=10**10
'''



def summation(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b
    
if __name__ == '__main__':
    
        a = int(input())
        b = int(input())
        
        if (1<=a<=10**10) and (1<=b<=10**10):
            print(summation(a,b))
            print(subtraction(a,b))
            print(multiplication(a,b))