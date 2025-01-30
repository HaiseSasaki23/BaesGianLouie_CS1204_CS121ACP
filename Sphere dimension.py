import math

diameter = int(input("What is the diameter? "))
radius = diameter/2
volume = 4/3 * math.pi * radius**3
area = 4* math.pi*radius**2

print(f"Diameter of the sphere: {diameter}")
print(f"Surface Area is {area:.4f}")
print(f"Volume is {volume:.4f}")