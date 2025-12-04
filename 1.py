# Finding the Sum of Digits of a Number Until Zero
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to repeatedly sum the digits of a number until the result is zero.
# Example:
# Input: number = 123
# Output: 6
# Explanation: Sum of digits is 1 + 2 + 3 = 6; sum of digits of 6 is 6 (which is a single digit).

def sum_of_digits_until_zero(number): # Function to sum digits until the result is zero
    while number > 0: # Continue until the number is zero
        digit_sum = sum(int(digit) for digit in str(number)) # Calculate the sum of digits
        number = digit_sum # Update number to the sum of its digits
    return number # Return the final result (which will be zero)
    # Example usage
input_number = 555 
result = sum_of_digits_until_zero(input_number)
print("Result:", result)    # Output: Result: 0 
print('hello world')