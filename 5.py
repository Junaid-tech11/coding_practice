# Generating a Diamond Pattern of Stars
# Difficulty: Medium
# Topics: Patterns, Basic Programming
# Description: Write a program to create a diamond pattern with stars of a given size.
# Example:
# Input: size = 5
# Output:

n = 5 # Example input size
for i in range(1, n + 1):
    # STEP: Calculate the number of spaces using N - i
    num_spaces = n - i
    
    # STEP: Calculate the number of stars using 2*i - 1
    num_stars = (2 * i) - 1


    # STEP: Print the concatenation of spaces and stars
    print(" " * num_spaces + "*" * num_stars)
        # STEP: Use a decreasing range from N-1 down to 1 (stop before 0)
for j in range(n - 1, 0, -1):
    # STEP: Calculate the number of spaces using N - j
    num_spaces = n - j
    
    # STEP: Calculate the number of stars using 2*j - 1
    num_stars = (2 * j) - 1

    # STEP: Print the concatenation of spaces and stars
    print(" " * num_spaces + "*" * num_stars)