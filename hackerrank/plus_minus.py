#Given an array of integers, calculate the ratios of its 
#elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

# [...] indicates that this is a list comprehension, meaning it will generate a list.
#essentially means "create a list containing all elements x from arr where x is greater than 0"
positive_elements = [x for x in arr if x > 0]
positive_count = len(positive_elements)

negative_elements = [x for x in arr if x < 0]
negative_count = len(negative_elements)

zero_elements = [x for x in arr if x == 0]
zero_count = len(zero_elements)

positive_ratio = positive_count / n
negative_ratio = negative_count / n
zero_ratio = zero_count / n

print("{:.6f}".format(positive_ratio))
print("{:.6f}".format(negative_ratio))
print("{:.6f}".format(zero_ratio))