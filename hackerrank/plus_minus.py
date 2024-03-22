#Given an array of integers, calculate the ratios of its 
#elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

arr = [-4, 3, -9, 0, 4, 1]  # Example array

n = len(arr)  # Find the length of the array

# Counters for positive, negative, and zero elements
positive_count = 0
negative_count = 0
zero_count = 0

for i in range(n):  # Iterate over the indices from 0 to n-1
    if arr[i] > 0:  # Check if the element at index i is greater than 0
        positive_count += 1
    elif arr[i] < 0:  # Check if the element at index i is less than 0
        negative_count += 1
    else:  # If the element at index i is not greater than 0 and not less than 0, it must be equal to 0
        zero_count += 1

# Calculate the ratios
positive_ratio = positive_count / n
negative_ratio = negative_count / n
zero_ratio = zero_count / n

# Print the ratios with 6 decimal places
print("{:.6f}".format(positive_ratio))
print("{:.6f}".format(negative_ratio))
print("{:.6f}".format(zero_ratio))
