# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Loops/problem/table-difference

"""
Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
Note: Don't add a new line in the end.

Input: n1 = 9, n2 = 4
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  9 18 27 36 45 54 63 72 81 90
- 4  8 12 16 20 24 28 32 36 40
-----------------------------------------
= 5 10 15 20 25 30 35 40 45 50
"""

def difference(n1,n2):
    for i in range(1, 11):
        diff = (i * n1) - (i * n2)
        if i < 10:
            print(diff, end=" ")
        else:
            print(diff, end=" ")