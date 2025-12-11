"""1.1.2. Sum of Digits of a Number

Write a Python program that reads an integer, calculates the sum of its digits, and prints the result.



Input Format:

The program reads an integer input with the prompt "Enter a number: "


Output Format:

Print the sum of the digits in the format:
Sum of digits: <digit_sum>


Note:

Some base code was provided (input and print statements). The task was to complete the missing logic.
"""
# Type Content here...
n =int(input ("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(abs(n)))
print(f"Sum of digits: {digit_sum}")
