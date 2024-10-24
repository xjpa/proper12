# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Loops/problem/for-loop-2

"""
You are given a String S, you need to print its characters at even indices(index starts at 0).

Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed.
"""

def utility(s):
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i], end="") 

# a pythonic approach would be to use slicing:
# print(s[::2])
# it prints every 2nd character of the string 
# but it prints with a newline, which we dont want
# so we have to use some join to edit output with end=""
def utility(s):
    print("".join(s[::2]), end="")
