# Exercise 33 - Day Old Bread

loaves = int(input("Enter number of day-old loaves: "))

price = 3.49
discount_rate = 0.60

regular = loaves * price
discount = regular * discount_rate
total = regular - discount

print(f"Regular price: ${regular:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"Total price: ${total:.2f}")