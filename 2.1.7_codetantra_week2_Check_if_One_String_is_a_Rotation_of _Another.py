"""2.1.7. Check if One String is a Rotation of Another

Write a program to check if one string is a rotation of another string.

Two strings are rotations of each other if they have the same length and one string can be obtained by rotating the other string any number of positions.



Input Format:

The first line prompts "Enter first string: " followed by a string 
.
The first line prompts "Enter second string: " followed by a string 
.


Output Format:

If the strings have different lengths, print:"""

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


# Check length first
if len(str1) != len(str2):
		print("Not a rotation (different lengths)")
else:
		# Check rotation by doubling the first string
		if str2 in (str1 + str1):
			print("Yes, the strings are rotations of each other")
		else:
			print("No, the strings are not rotations of each other")