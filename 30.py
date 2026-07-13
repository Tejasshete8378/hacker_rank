"""
PROBLEM STATEMENT : Itemized Price Aggregator using OrderedDict
---------------------------------------------------------------------------------------------
Objective:
--------------
To store and aggregate the prices of multiple items provided by the user while maintaining the 
insertion order using an OrderedDict.

Constraint:
--------------
- The input consists of an item name (which may contain multiple words) and a price integer.
- The item name is defined as all tokens before the last token, and the price is the last token.
- If an item already exists in the collection, its price should be added to the existing total.

Input:
--------------
- An integer 'n' representing the number of entries.
- 'n' lines of strings, each containing an item name (e.g., "BANANA 10") or 
  multi-word names (e.g., "APPLE FRUIT 20").

Output:
--------------
- A formatted list of unique items and their accumulated total prices, printed in the order 
  they were first entered.

Task:
--------------
Develop a script that parses user input to separate item names from their respective prices, 
aggregates prices for duplicate item entries, and displays the final catalog using 
OrderedDict to preserve input sequence.
"""


from collections import OrderedDict

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    
    n = int(input("Enter Number of Items: "))
    print()
    data = OrderedDict()

    for i in range(n):
        name = input("Enter Name and Price: ").split()
        print()
        new_name = " ".join(name[0:-1])
        price = int(name[-1])

        if new_name in data:
            data[new_name] = data[new_name] + price
        else:
            data[new_name] = price

    print("Your Items and their Prices are as Follows: ")
    print()
    for name, price in data.items():
        print(f"Item Name = {name} and Item Price = {price}")
        print()

    print('\n','*'*30,"Thank You",'*'*30,'\n')