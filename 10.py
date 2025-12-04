# Finding the Number of Perfect Numbers Up to a Given Limit
# Difficulty: Medium
# Topics: Number Theory
# Description: Write a program to find how many perfect numbers exist up to a given limit.
# Example:
# Input: limit = 30
# Output: 1
# Explanation: There is only one perfect number (6) up to 30.

n= int(input("Enter a Number: "))
perfect_count= 0

for i in range(1, n+1):
    divisor_sum = 0
    for j in range(1,i):
        if i%j==0:
            divisor_sum +=j
        
    if divisor_sum == i:
        perfect_count +=1
    
print(perfect_count)