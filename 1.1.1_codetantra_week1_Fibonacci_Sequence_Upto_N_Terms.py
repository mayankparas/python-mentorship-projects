"""1.1.1. Fibonacci Sequence Upto N Terms
32:38
Write a Python program that takes an integer 
 and prints the Fibonacci series up to the 
 term.



Input Format:

The program should prompt the user with: "Enter the number of terms: "
The input consists of a single integer 
, representing the number of terms in the Fibonacci sequence to print.


Output Format:

If 
, print: "Please enter a positive integer"
If 
, print
Fibonacci sequence up to 1 term:
0
For 
, print
Fibonacci sequence up to n terms:
0 1 1 2 3 ... 
(The sequence should be printed on the same line, with each number separated by a space.)

Ensure the output ends with a newline.


Constraints:



Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""
# Type Content here...
a=0
b=1
n = int(input("Enter the number of terms: "))

# Handle invalid input
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print(f"Fibonacci sequence up to {n} terms:")
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b

        count += 1
    print()