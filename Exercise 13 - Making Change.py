# Exercise 13 - Making Change

cents = int(input("Enter the number of cents: "))

toonies = cents // 200
cents %= 200

loonies = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print("Toonies:", toonies)
print("Loonies:", loonies)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
