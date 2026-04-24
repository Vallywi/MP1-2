# Exercise 25 - Units of Time (Again)

number_seconds = int(input("Enter the number of seconds: "))
days = number_seconds // (24 * 3600)
number_seconds = number_seconds % (24 * 3600)
hours = number_seconds // 3600
number_seconds = number_seconds % 3600
minutes = number_seconds // 60
number_seconds = number_seconds % 60
print(f"{days} days, {hours} hours, {minutes} minutes, and {number_seconds} seconds")
