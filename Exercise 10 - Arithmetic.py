# Exercise 10 - Arithmetic

import math

a = input("Enter first number: ")
b = input("Enter second number: ")

sum_result = int(a) + int(b)
print("The sum of the two numbers is:", sum_result)

difference_result = int(a) - int(b)
print("The difference of the two numbers is:", difference_result)

product_result = int(a) * int(b)
print("The product of the two numbers is:", product_result)

quotient_result = int(a) / int(b)
print("The quotient of the two numbers is:", quotient_result)

remainder_result = int(a) % int(b)
print("The remainder of the two numbers is:", remainder_result)

log_result = math.log10(int(a))
print("The log10(a) is:", log_result)

power_result = int(a) ** int(b)
print("The power of two numbers is:", power_result)
