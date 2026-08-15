from math import sqrt, pow

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print("The distance between the two points is:", round(distance, 2))

# Reflection: 
# Using the math library makes the program easier because sqrt() and pow() do the calculations for me
# Without these functions, I would have to write more calculations by my own.
