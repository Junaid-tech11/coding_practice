# Finding the Sum of the First N Prime Numbers
# Difficulty: Medium
# Topics: Prime Numbers, Mathematical Computations
# Description: Write a program to calculate the sum of the first N prime numbers.
# Example:
# Input: N = 4
# Output: 17
# Explanation: The sum of the first 4 prime numbers (2 + 3 + 5 + 7) is 17.

# n= 4
# count = 0
# sum_value = 0
# current_number =  2

# while count < n:
#     is_prime = True
#     for i in range(2, current_number):
#             if current_number% i ==0:
#                     is_prime = False
#     if is_prime == True:
#         sum_value += current_number
#         count +=1

    
#     current_number +=1
# print(sum_value)



sum_value = 0


for number in range(2, 100+1):
    is_prime = True
    for i in range(2, number):
            if number% i ==0:
                    is_prime = False
    if is_prime == True:
        sum_value += number
        

    
    
print(sum_value)