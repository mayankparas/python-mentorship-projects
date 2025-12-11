"""3.1.1. Sort a List in Ascending Order Without Using sort()
You are given a list of integers as input. Your task is to sort this list in ascending order, without using any built-in sorting functions like sort() or sorted().



Input Format:

A single line of space-separated integers.


Output format:

The first line prompts "Original list: " followed by the original list of numbers.
The second line prompts "Sorted list (ascending): " followed by the sorted list.


Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""
input_str = input("Enter numbers separated by space: ")

numbers = list(map(int, input_str.split()))

print("Original list:", numbers)

# Manual sorting (Bubble Sort)
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list (ascending):",numbers)
