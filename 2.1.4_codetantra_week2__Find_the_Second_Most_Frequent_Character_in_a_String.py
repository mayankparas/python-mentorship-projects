"""2.1.4. Find the Second Most Frequent Character in a String
00:33
Write a Python program that reads a string from the user and finds the second most frequent character in the string. If no such character exists (i.e., the string has fewer than two unique characters), the program should display an appropriate message.



Input Format:

The program should prompt the user with: "Enter a string: " followed by a string (which may include letters, digits, symbols, or whitespace).


Output Format:

If there is a valid second most frequent character, print:
Second most frequent character: <character>"""
text = input("Enter a string: ")
# Count frequency of each character
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1


# Sort by frequency (highest first)
sorted_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_freq) < 2:
	print("No second most frequent character found")
else:
	second_char, second_count = sorted_freq[1]

	print("Second most frequent character:",second_char)
	print("Frequency:",second_count)