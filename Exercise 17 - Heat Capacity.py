# Exercise 17 - Heat Capacity

mass = float(input("Enter mass of water: "))
temp1 = float(input("Enter initial temperature of water: "))
temp2 = float(input("Enter final temperature of water: "))

energy = mass * 4.186 * (temp2 - temp1)
print("The total amount of energy (J) is:", energy)

kwh = energy / 3600000
print("Energy in kWh:", kwh)

cost = kwh * 8.9
print("Cost in cents:", round(cost, 2))
