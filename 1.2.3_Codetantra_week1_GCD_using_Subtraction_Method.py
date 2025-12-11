"""1.1.3. GCD using Subtraction Method
Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using the subtraction method.

Input Format:

The first line contains: "Enter first number: " followed by an integer input.
The second line contains: "Enter second number: " followed by an integer input.


Output Format:

Print the result in the format: "GCD is: <value>"


Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Type Content here...
while a != b:
    if a > b:
        a -= b
    else:
        b -= a




print("GCD is:", a )