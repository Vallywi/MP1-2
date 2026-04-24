# Exercise 4 - Area of a Field
w,l = map(float, input("Enter width and length of the farm field (in feet) separated by space: ").split())
print (f"Width: {w} ft.")
print (f"Length: {l} ft.")
area = w*l 
acre = area/43560
print (f"The area of the field is {acre:.2f} acres.")