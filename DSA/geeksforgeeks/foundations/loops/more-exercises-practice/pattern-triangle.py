"""
1. get input
2. print row
3. should be reverse
"""

user_input = int(input())

for i in range(user_input):
    for j in range(i + 1):
        print("*", end= " ")
    print()

"""
input: 3
output:
* 
* * 
* * * 
"""