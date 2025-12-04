# Finding All Pairs of Elements in an Array that Add Up to a Given Sum
# Difficulty: Medium
# Topics: Arrays, Hashing
# Description: Write a program to find all pairs of elements in an array whose sum equals a specified target.
# Example:
# Input: array = [1, 2, 3, 4, 5], target = 5
# Output: [(1, 4), (2, 3)]
# Explanation: Pairs that sum up to 5 are (1, 4) and (2, 3).

array = [1,2,3,4,5]
# n = len(array)
# target = 5
# result = []

# for i in range(0, n -1):
#     for j in range(i + 1, n):
#         test_sum = array[i]+ array[j]
#         if test_sum == target:
#             result.append((array[i], array[j]))

# print(f"Pairs that sum to {target}: {result}")

seen_num =set()
n = len(array)
results_pair = []
target  = 5

for i in range(n):
    current_sum = array[i]
    complement = target - current_sum
    if complement in  seen_num:
        results_pair.append((current_sum, complement))
    seen_num.add(current_sum)
print(f"The final result is {results_pair}")



