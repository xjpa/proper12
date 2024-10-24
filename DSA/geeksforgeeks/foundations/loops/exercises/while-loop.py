# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Loops/problem/while-loop
"""
Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
Input: 3
Output: 3 2 1 0
Explanation: Numbers in decreasing order from 3 are 3 2 1 0.
""" 

def utility(x):
    while x >= 0:
        print(x, end=" ")
        x = x - 1

# i think though that this is more pythonic
# as we dont need to manually subtract each iteration and just do it in range()
# which makes it more readable.
# nonetheless, the problem i solved calls for a while loop

def utility(x):
    for i in range(x, -1, -1):
        print(i, end=" ")


# so at best i can just use a shorthand for:
#  x = x - 1
# to shorten it to make it more pythonic, as such:
# x -= 1