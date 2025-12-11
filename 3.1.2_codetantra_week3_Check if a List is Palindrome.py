"""3.1.2. Check if a List is Palindrome
You are given a list of integers. Your task is to determine whether the list is a palindrome.

Input Format:

A single line of space-separated integers.


Output Format:

First, print the list in the format: "List: [elements]"
If the list is a palindrome then it prints: "List is a palindrome"
Otherwise print: "List is not a palindrome"


Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""

input_str = input()
lst = list(map(int, input_str.split()))
print("List:", lst)

# Type Content here...

# Check if list is palindrome
if lst == lst[::-1]:
	print("List is a palindrome")
else:
	
	print("List is not a palindrome")