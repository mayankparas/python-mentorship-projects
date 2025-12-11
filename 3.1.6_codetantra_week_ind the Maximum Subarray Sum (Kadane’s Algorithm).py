"""3.1.6. Find the Maximum Subarray Sum (Kadane’s Algorithm)

You are given an array of integers. Your task is to find the maximum possible sum of any contiguous subarray using Kadane's Algorithm.



Input Format:

A single line of space-separated integers representing the elements of the array.


Output Format:

The first line prints "Array: " followed by the original list of integers.
The second line prints "Maximum subarray sum: " followed by the maximum sum of any contiguous subarray.


Note:

Some base code was provided (print statements). The task was to complete the missing logic."""

arr = list(map(int, input().split()))

print("Array:",arr)
# Kadane's Algorithm
max_ending_here = arr[0]
max_so_far = arr[0]

for i in range(1, len(arr)):
    max_ending_here = max(arr[i], max_ending_here + arr[i])
    max_so_far = max(max_so_far, max_ending_here)


print("Maximum subarray sum:",max_so_far)