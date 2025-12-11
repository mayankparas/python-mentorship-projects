"""2.1.2. Replace Spaces with Underscore
11:16
Write a Python program that take
Write a Python program that takes a string input from the user and replaces all the spaces in the string with underscores (_). Then print the modified string.

Input Format:

The program should prompt the user with: "Enter a string: "
The input consists of a single line containing the string (which may include spaces).

Output Format:

Print the modified string in the format:
Modified string: <modified_string>
where <modified_string> is the original string with all spaces replaced by underscores.



Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""

text = input("Enter a string: ")
#Type your code here...
modified_string = text.replace(" ", "_")
print("Modified string:",modified_string)