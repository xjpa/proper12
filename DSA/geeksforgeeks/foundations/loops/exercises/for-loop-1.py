# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Loops/problem/for-loop-1

"""
You are given a number n, you need to print its multiplication table in a single line.
Input:
n = 6
Output:
6 12 18 24 30 36 42 48 54 60
"""

n=int(input())
## in is a membership operator that is true if something is a member of sequence
for i in range(1, 11):  # range is (inclusive, exclusive) or basically (x, y-1)
    ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
    print(i*n, end=" ") 

# perhaps a more pythonic way would be to 
# use join() to concatenate then combine it with
# generator expression  (str(i * n) for i in range(1, 11)

n = int(input())
print(" ".join(str(i * n) for i in range(1, 11)))

# a benefit of join is it leaves no trailing space compared to:
# print(i*n, end=" ") 
# cos join() auto joins the elements with exactly one space between them. 