"""2.1.5. Anagram Check
Write a Python program to check whether two input strings are anagrams of each other.
Input Format:
The program should prompt the user with:
Enter first string:
Enter second string:
Each input consists of a line of text (may include letters, spaces, or mixed case).

Output Format:
If the strings are anagrams, print: "The strings are anagrams"
Otherwise, print: "The strings are not anagrams"

Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", "")):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")