

import cmath
import math

if __name__ == '__main__':
    print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')
    comp1 = float(input("Enter Real Part of Complex Number: "))
    print()
    comp2 = float(input("Enter Imaginary Part of Complex Number: "))
    print()
    
    comp = complex(comp1,comp2)
    print(f"Your Complex Number is: {comp}")
    print()

    phs1 = cmath.phase(comp)
    abso = abs(comp)
    phs2 = math.degrees(phs1)

    print(f"Modulus = {abso}")
    print()
    print(f"Phase Angle in Radians = {phs1}")
    print()
    print(f"Phase Angle in Degree = {phs2}")
    print('\n','*'*30,"Thank You",'*'*30,'\n')

    '''The cmath.phase function returns the angle in radians. 
    If you ever need it in degrees for engineering documentation, 
    you can easily convert it using math.degrees(phs).'''