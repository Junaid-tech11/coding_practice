# Finding the GCD of Multiple Numbers
# Difficulty: Medium
# Topics: Mathematical Computations
# Description: Write a program to find the GCD (Greatest Common Divisor) of an array of numbers.
# Example:
# Input: array = [12, 24, 36]
# Output: 12
# Explanation: The GCD of 12, 24, and 36 is 12.
array = [12, 24, 36]

def gcd(a,b):
    while b > 0:
        n = a % b
        a = b
        b = n
    return a
        
def find_gcd(array):
    result = array[0]

    for i in array[1:]:
        result = gcd(result, i)

    return result
answer = find_gcd(array)

print(answer)
