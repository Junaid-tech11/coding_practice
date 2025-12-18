# Generating a Matrix with a Spiral Pattern
# Difficulty: Medium
# Topics: Arrays, Matrix Operations
# Description: Write a program to generate a matrix filled with numbers in a spiral pattern.
# Example:
# Input: size = 3
# Output:

# 1 2 3  
# 8 9 4  
# 7 6 5  

size = 5
matrix = [[0] * size for _ in range(size)]  # Initialize a size x size matrix with zeros
left, right = 0, size - 1    # Initialize boundaries
top, bottom = 0, size - 1   # Initialize boundaries
num = 1
while left <= right and top <= bottom:  # Fill the matrix in a spiral order
    for i in range(left, right + 1):    # Fill top row
        matrix[top][i] = num    # Fill top row
        num += 1         # Increment number
    top += 1

    for i in range(top, bottom + 1):  # Fill right column
        matrix[i][right] = num       
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
for row in matrix:
    print(" ".join(map(str, row)))
# 1 2 3  
# 8 9 4     
# 7 6 5
