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






