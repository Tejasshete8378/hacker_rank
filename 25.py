import cmath

if __name__ == '__main__':

    comp = complex(input("Enter Complex Number: "))
    print()

    phs = cmath.phase(comp)
    abso = abs(comp)

    print(f"Modulus = {abso}")
    print()
    print(f"Phase Angle = {phs}")
    print()