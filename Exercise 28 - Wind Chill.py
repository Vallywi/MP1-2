# Exercise 28 - Wind Chill

temp = float(input("Enter temperature (°C): "))
wind = float(input("Enter wind speed (km/h): "))

wci = 13.12 + 0.6215 * temp - 11.37 * (wind ** 0.16) + 0.3965 * temp * (wind ** 0.16)

print("Wind Chill Index:", round(wci))