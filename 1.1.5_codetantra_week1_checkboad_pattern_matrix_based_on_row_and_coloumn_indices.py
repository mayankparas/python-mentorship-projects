"""1.1.5. Print a Checkerboard Pattern Matrix Based on Row and Column Indices
Write a Python program that takes two integers, 
 and 
, representing the number of rows and columns respectively, and prints an 
 matrix where the value of each element depends on the sum of its row and column indices:

Print "1" if the sum of the current row index and column index is even.
Print "0" if the sum is odd.


Input Format:

The first line prompts "Enter the number of rows: " followed by an integer 
 representing the number of rows.
The second line prompts "Enter the number of columns: " followed by integer 
 representing the number of columns.


Output Format:

Print the matrix of size 
.
Each row should be printed on a new line.
Elements in each row should be separated by a single space."""
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))


# Generate and print matrix
for i in range(n):
    for j in range(m):
        # 1 if (n+m) even, 0 if odd
        if (i + j) % 2 == 0:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()  # Newline after each row






