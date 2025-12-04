# Generating a Matrix with Multiplication Table
# Difficulty: Easy
# Topics: Arrays, Matrix Operations
# Description: Write a program to generate a matrix where each element at position (i, j) is the product of i and j.
# Example:
# Input: size = 3
# Output:
# 1 2 3
# 2 4 6
# 3 6 9

N = int(input("Enter a Number: "))
matrix = []

for i in range(1, N+1):
    current_row=[]

    for j in range(1, N+1):
        product = i*j
        current_row.append(product)
    matrix.append(current_row)

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()