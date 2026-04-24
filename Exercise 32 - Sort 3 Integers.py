# Exercise 32 - Sort 3 Integers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

small = min(a, b, c)
large = max(a, b, c)
middle = a + b + c - small - large

print("Sorted:", small, middle, large)