# Exercise 15 - Distance Units

measurement = float(input( "Enter measurement(in feet): "))

feet_inches = measurement * 12
print ("Feet to inches: ", feet_inches)

feet_yards = measurement / 3
print (f"Feet to yards: {feet_yards:.4f}")

feet_miles = measurement / 5280
print (f"Feet to miles: {feet_miles:.4f}")
