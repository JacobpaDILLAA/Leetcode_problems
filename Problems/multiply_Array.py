# PROBLEM:
# Given an array of integers, return a new array 
# such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].

# TEST CASE:
# Thought process on this was to iterater over the array. 
# The next phase was to make sure the number didn't math the 
# number in the specific place for this i would use an if statement 
# Lastly append the multiplied value to the new array

def mul(container):
  solution = []
  for i in range(len(container)):
    temp = 1
    for j in container:
      if j != container[i]:
        temp *= j
    solution.append(temp)
  return solution

container = [1, 2, 3, 4, 5]
ans = mul(container)
print(ans)