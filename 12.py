# Generating a Matrix of Fibonacci Numbers
# Difficulty: Medium
# Topics: Arrays, Matrix Operations
# Description: Write a program to generate a matrix where each element is a Fibonacci number.
# Example:
# Input: size = 3
# Output:

# 1 1 2  
# 3 5 8  
# 13 21 34  
#fib is defined as sum of previous two numbers:
def fib(n):
    if n <= 1 or n ==0:
        return n
    else:
        return fib(n-1) + (fib(n-2))
    
v = fib(7)
print(v)

