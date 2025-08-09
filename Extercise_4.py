# Calculate area (A = πr²) of a circle

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of a circle is : {round(area, 2)}cm²")