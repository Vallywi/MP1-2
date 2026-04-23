# Exercise 23 - Area of a Regular Polygon

import math

side_length = float(input("Enter the length of the side of the equilateral triangle: "))
side_number = int(input("Enter the number of sides of the polygon: "))

def calculate_area(side_length, side_number):
    area = (side_number * (float(side_length) ** 2)) / (4 * math.tan(math.pi / float(side_number)))
    return area
a = calculate_area(side_length, side_number)

print(f"The area of the polygon is: {a} ")  
