# Finding the Sum of the First N Odd Numbers
# Difficulty: Easy
# Topics: Mathematical Computations
# Description: Write a program to calculate the sum of the first N odd numbers.
# Example:
# Input: N = 5
# Output: 25
# Explanation: Sum of the first 5 odd numbers (1 + 3 + 5 + 7 + 9) is 25.




num = int(input("Enter the Number for Sum: "))
total_sum = 0
for i in range(num):
    odd = (2*i+1)
    total_sum += odd
    
print(total_sum)


#Method 2
num = int(input("Enter the Number for Sum: "))
print(num * num)