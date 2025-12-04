# Finding the Longest Consecutive Sequence in an Array
# Difficulty: Medium
# Topics: Arrays, Hashing
# Description: Write a program to find the longest sequence of consecutive numbers in an array.
# Example:
# Input: array = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4].

array = [100, 4, 200, 1, 3, 2]
my_set = set(array)
longest_streak = 0

for num in my_set:
    if num-1 in my_set:
        continue
    if num - 1 not in  my_set:
        current_num = num
        current_streak = 1
        while current_num + 1  in my_set:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

print(longest_streak)



