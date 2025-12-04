# Finding the Sum of Numbers in a String
# Difficulty: Easy
# Topics: String Manipulation
# Description: Write a program to extract and sum all numbers present in a given string.
# Example:
# Input: string = "The numbers are 12 and 34"
# Output: 46
# Explanation: The sum of numbers 12 and 34 is 46.

input_string = "The numbers are 12 and 34"
sum_value = 0
current_number = ""
for char in input_string:
    if char.isdigit():
        current_number += char
    else:
        if current_number != "":
            sum_value += int(current_number)
            current_number = ""
if current_number != "":
    sum_value += int(current_number)
print(sum_value)

print("-------------")
