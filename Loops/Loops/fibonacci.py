# Program to Print Fibonacci Series

n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print(a)
else:
    print("Fibonacci Series:")
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
