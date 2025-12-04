# Generating a Multiplication Table for a Range
# Difficulty: Easy
# Topics: Arrays, Basic Programming
# Description: Write a program to generate multiplication tables for numbers within a specified range.
# Example:
# Input: start = 2, end = 4
# Output:
# 2 x

def generate_multiplication_table(start, end): # Function to generate multiplication tables
    tables = {} # Dictionary to hold multiplication tables
    for i in range(start, end + 1): # Loop through the specified range
        table = [] # List to hold the multiplication table for the current number
        for j in range(1, 11): # Generate multiplication table from 1 to 10
            table.append(f"{i} x {j} = {i * j}") # Append formatted string to the table list
        tables[i] = table # Add the table to the dictionary
    return tables # Return the dictionary of multiplication tables

# Example usage
start_number = 2    
end_number = 4
multiplication_tables = generate_multiplication_table(start_number, end_number)
for number, table in multiplication_tables.items(): # Loop through the generated tables
    print(f"Multiplication Table for {number}:") # Print header
    for line in table: # Print each line of the multiplication table
        print(line)
    print() # Print a newline for better readability 1 = 2
# 2 x 2 = 4
# 3 x 1 = 3
# 3 x 2 = 6                     
# 4 x 1 = 4
# 4 x 2 = 8
# 2 x 3 = 6