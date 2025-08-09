# find the hypotenuse (c = √(a² + b²)) of a triangle
import math

a = float(input("Enter the length of side A : "))
b = float(input("Enter the length of side B : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C is : {round(c, 2)}cm")

