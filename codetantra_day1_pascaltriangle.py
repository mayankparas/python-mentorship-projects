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
