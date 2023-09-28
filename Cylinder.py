import math
radius = float(input("Please enter the radius of the cylinder: "))
height = float(input("Please enter the height of the cylinder: "))
print("Surface area of cylinder: " + str( (2 * math.pi * radius**2) + 2*radius * math.pi * height) )
