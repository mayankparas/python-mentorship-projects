"""2.1.6. Longest Common Prefix of a String
Write a Python program that reads a list of strings from the user and prints the Longest Common Prefix (LCP) shared by all the strings. The longest common prefix is the longest starting substring that is common to all given words. If no such prefix exists, the program should return "-1".
Input Format:
The first line contains a single integer 
 — the number of strings.
The second line contains 
 space-separated strings consisting of lowercase or mixed-case letters.


Output Format:

Print the list of input strings in the format:
Words: [word1, word2, ..., wordn]
Then, print the longest common prefix in the format:
Longest Common Prefix: <prefix>
If no common prefix exists print "-1".


Note:

Some base code was provided (input and print statements). The task was to complete the missing logic."""

n = int(input())
words = input().split()

print("Words:", words)

if not words:
    print("Longest Common Prefix: -1")
else:
    prefix = words[0]

    for w in words[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                break

    if prefix == "":
        print("Longest Common Prefix: -1")
    else:
        print("Longest Common Prefix:", prefix)