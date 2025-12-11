"""2.1.3. Shortest Word in a String
Write a Python program that reads a string from the user, finds the shortest word in the string, and prints it.



Input Format:

The program should prompt the user with: "Enter a string: "
The input consists of a single line containing one or more words separated by spaces.


Output Format:

Print the shortest word in the input string in the format:
Shortest word: <word>
where <word> is the shortest word found.



Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""
text = input("Enter a string: ")
# Type Content here...
words = text.split()
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)