# Exercise 16 - Area and Volume

import math
radius = float(input("Enter radius of the cirle: "))

area = math.pi * radius ** 2
print (f"Area of the circle: {area:.2f}", )

volume = (4/3) * math.pi * (radius ** 3)
print (f"Volume of the circle: {volume:.2f}", )
