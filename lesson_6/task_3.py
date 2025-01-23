import math

number = int(input("Enter integer number:"))

while number > 9:
    digits = [int(d) for d in str(number)]
    number = math.prod(digits)

print(f"Multiplication of your number: {number}")



# Second solution (without importing math)
# number = int(input("Enter integer number:"))
#
# multiplication = 1
# while number > 9:
#     for digit in str(number):
#         multiplication *= int(digit)
#     number = multiplication
#     multiplication = 1
#
# print(f"Multiplication of your number: {number}")

