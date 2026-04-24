# Exercise 30 - Units of Pressure

kpa = float(input("Enter pressure (kPa): "))

psi = kpa * 0.145038
mmhg = kpa * 7.50062
atm = kpa / 101.325

print("PSI:", psi)
print("mmHg:", mmhg)
print("Atmospheres:", atm)