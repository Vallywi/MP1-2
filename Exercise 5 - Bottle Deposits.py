# Exercise 5 - Bottle Deposits
print (f"{'SMALL CONTAINERS: 1 LITER OR LESS':>10}")
print (f"{'LARGE CONTAINERS: MORE THAN 1 LITER':>10}\n")
small = int(input("Enter number of small container: "))
large = int(input("Enter number of large container: "))

refund1 = small*0.10
refund2 = large*0.25
print (f"\nYou received ${refund1:.2f} for returning small container")
print (f"You received ${refund2:.2f} for returning large container")
print (f"You received a total of ${refund1+refund2:.2f} refund for returning these containers.")
