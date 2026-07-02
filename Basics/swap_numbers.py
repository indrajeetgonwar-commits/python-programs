# Program to Swap Two Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nBefore Swapping")
print("First Number =", num1)
print("Second Number =", num2)

# Swapping
temp = num1
num1 = num2
num2 = temp

print("\nAfter Swapping")
print("First Number =", num1)
print("Second Number =", num2)
