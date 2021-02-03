# PROBLEM: 
# Given a list of numbers and a number k, return whether any two numbers # from the list add up to k. For example, given [10, 15, 3, 7] and k of # 17, return true since 10 + 7 is 17.

# TEST CASE:
# container is empty or has 1 number return False since the problem needs two numbers. If the container has 2 numbers now we can figure out the problem by taking the key and subtracting the value in the ith postion. From this we can see if the number is in the container 

container = [10,15,3,7]
key = 17

for i in container:
    if key - i in container:
        solution = "true"
    else:
        solution = "false"

print(solution)