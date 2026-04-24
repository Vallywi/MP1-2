# Exercise 6 - Tax and Tip
meal = int(input("Enter meal cost: P"))
tax = meal * 0.12
tip = meal * 0.18
grandtotal = meal+tax+tip
print ("\n------------------------------")
print (f"Tax Amount: P{tax:.2f}")
print (f"Tip Amount: P{tip:.2f}")
print (f"Grand Total: P{grandtotal:.2f}")
print ("------------------------------")