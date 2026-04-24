# Exercise 9 - Compound Interest
from datetime import datetime
today = datetime.now()
deposit = float(input("Enter amount of money to be deposited: P"))

print (f"\n----- {today:%B %d, %Y} ", end=" || ")
print (f" {today:%H:%M:%S %p} -----", end="\n")
print (f"----- You deposited P{deposit:.2f} -----")
print ("\n****** Your savings of will have an interest of 4% every year ******")

rate = 0.04

print (f"Savings after 1 year: {deposit*(1+rate)**1:.2f}")
print (f"Savings after 2 years: {deposit*(1+rate)**2:.2f}")
print (f"Savings after 3 years: {deposit*(1+rate)**3:.2f}")