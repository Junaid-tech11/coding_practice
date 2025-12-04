# Finding the Largest Prime Factor of a Number
# Difficulty: Medium
# Topics: Number Theory
# Description: Write a program to find the largest prime factor of a given number.
# Example:
# Input: number = 28
# Output: 7
# Explanation: The prime factors of 28 are 2 and 7, with the largest being 7.

import math

n = int(input("Enter the Number: "))

# Initialize variable to avoid errors if n is small
largest_factor = n 

# Step 1: Handle the smallest prime (2)
while n % 2 == 0:
    largest_factor = 2
    n = n // 2

# Step 2: Handle the odd numbers
# Optimization: Only go up to the square root of n
# Optimization: Step by 2 to skip even numbers (3, 5, 7...)
for i in range(3, int(math.sqrt(n)) + 1, 2):
    
    # If we reduced n to 1, we can stop early
    if n == 1:
        break

    while n % i == 0:
        largest_factor = i
        n = n // i

# Step 3: The leftover
# If n is still > 2, the remaining n is a prime number (and the largest factor)
if n > 2:
    largest_factor = n

print(f"The largest prime factor is: {largest_factor}")