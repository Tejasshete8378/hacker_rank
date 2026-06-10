thickness = int(input ("Enter Thickness: "))
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness - 1) + c + (c*i).ljust(thickness - 1))

# Top pillars
for i in range(thickness):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))