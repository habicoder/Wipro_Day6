
def FindAutoCount(n):
     if n is None:
         return 0

     digit_counts = [0] * 10  # Initialize an array to store counts of digits 0-9

     for digit in n:
         digit_counts[int(digit)] += 1  # Increment the count for each digit in the input

     distinct_numbers = 0
     for i, count in enumerate(digit_counts):
         if count > 0:
             distinct_numbers += 1  # Count the distinct numbers present in the input

     return distinct_numbers if n == ''.join(str(digit_counts[i]) for i in range(10)) else 0

# # Example usage:
input_str = "1210"
output = FindAutoCount(input_str)
print(output)  # Output: 3

 
