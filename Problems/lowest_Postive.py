# PROBLEM:
# Given an array of integers, find the first missing positive integer 
# in linear time and #constant space. In other words, find the lowest positive 
# integer that does not exist in the #array. The array can contain duplicates 
# and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.

# TEST CASE:
# Here we can put all values in a set to make it constant
# For the linear portion a simple for loop would take care of it. 

def lowest_positive(array):
  num = set(array)
  for i in range (1, len(array)+1):
    if i not in num:
      return i
  
test_one = [3,4,-1,1,1]
print("Solution: ",lowest_positive(test_one))

# test_two = [1,2,0]
# print(lowest_positive(test_two))

