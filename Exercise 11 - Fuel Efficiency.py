# Exercise 11 - Fuel Efficiency

mpg = float(input("Enter fuel efficiency in MPG: "))

conversion_factor = 235.215
l_per_100km = conversion_factor / mpg

print("MPG:", mpg)
print("Converted to L/100 km:", round(l_per_100km, 2))
