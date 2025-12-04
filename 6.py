# Counting the Number of Palindromic Substrings in a String
# Difficulty: Medium
# Topics: String Manipulation
# Description: Write a program to count how many palindromic substrings exist in a given string.
# Example:
# Input: string = "aaa"
# Output: 6
# Explanation: Palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".



def count_substring(s):
    count = 0   
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count    
string = "abbac"
result = count_substring(string)
print(result)