"""1.1.4. Pascal's Triangle
Write a python program to print Pascal's Triangle up to the 
 row.



Input Format:

The input consists of a single integer 
, which represents the number of rows of Pascal's Triangle to print.
The input prompt should be: "Enter number of rows: "


Output Format:

Print the first 
 rows of Pascal's Triangle, with each row printed on a new line
The numbers in each row should be separated by a single space.
Each row should be indented with spaces so that the triangle shape is maintained.


Note:

For better understanding of the output format, refer to the sample test cases."""
n = int(input("Enter number of rows: "))

for i in range(n):
    # Exactly 5 spaces first row (n-i spaces)
    print(' ' * (n - i), end='')
    
    # Print coefficients with spaces between AND trailing space
    coef = 1
    for j in range(i + 1):
        print(coef, end=' ')
        coef = coef * (i - j) // (j + 1)
    
    print()
