# Checking for a Balanced Bracket Sequence
# Difficulty: Medium
# Topics: String Manipulation, Stack
# Description: Write a program to check if a given string with brackets is balanced.
# Example:
# Input: string = "{[()]}"
# Output: True
# Explanation: The brackets are balanced.

start = []
pairs = {')': '(', ']': '[', '}': '{'}
s = "{[()]}"

is_balanced = True


for char in s:
    if char in "( { [":
        start.append(char)
    elif char in ") } ]":
            if len(start) ==0:
                is_balanced = False
                break
            last_open =start.pop()
            expected_open = pairs[char]
            
            if last_open != expected_open:
                is_balanced = False
                break   

if is_balanced == True and len(start) ==0:
    print("True")
else:
    print("False")