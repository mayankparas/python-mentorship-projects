"""2.1.1. Remove Vowel
02:36
You are given a word. Your task is to remove all the vowels from the word and return the modified word.



Input Format:

The input is a string representing the word.


Output Format:

The output is the modified string without any vowels.
Docstring for Codetantra_day2_vowels_remove
"""
word = input()

vowels = "aeiouAEIOU"
result = ""

for ch in word:
    if ch not in vowels:
        result += ch

print(result)