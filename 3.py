# Calculating the Sum of a Series (1 + 1/2 + 1/3 + ... + 1/n)
# Difficulty: Medium
# Topics: Mathematical Computations
# Description: Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.
# Example:
# Input: n = 4
# Output: 2.083333
# Explanation: Sum of the series is 1 + 1/2 + 1/3 + 1/4 ≈ 2.083333.

# n = int(input("Enter the number of the sum of the series : "))
# harmonic_sum = 0.0

# for i in range(1, n+1):
#     harmonic_sum =  harmonic_sum + 1.0/i
    
#     print(f"sum of series is {harmonic_sum}")

# Sum of Squares Reciprocal: Calculate the series $1 + \frac{1}{4} + \frac{1}{9} + \dots + \frac{1}{n^2}$. 
# (Hint: only the $\frac{1}{i}$ part changes).
# n = int(input("Enter the number for the sum of squares: "))
# square_reciprocal = 0.0

# for i in range(1, n+1):
#     square_reciprocal += 1.0 / (i**2)
#     print(f"sum of series is {square_reciprocal}")


n = int(input("Enter the number of terms: "))
# Renaming the accumulator is helpful, but optional
alt_harmonic_sum = 0.0 

for i in range(1, n + 1):
    # This single line handles both the sign AND the division
    alt_harmonic_sum += (-1)**(i + 1) * (1.0 / i) 
    
    # You can print the running total inside, or move it outside
    print(f"Running sum is: {alt_harmonic_sum}")