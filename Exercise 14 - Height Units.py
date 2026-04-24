# Exercise 14 - Height Units

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

feet_inches = feet * 12
total_inches = feet_inches + inches

inches_cm = total_inches * 2.54

print("Height in centimeters: ", inches_cm)
