#Piling Up!
#https://www.hackerrank.com/challenges/piling-up/problem

import math

def stackable(lst):
    ans = 'Yes'
    prev = max([lst[0],lst[-1]])
    if prev == lst[0]:
        del lst[0]
    else:
        del lst[-1]

    while(lst != []):
        new_max = max([lst[0], lst[-1]])
        if new_max <= prev:
            prev = new_max
            if prev == lst[0]:
                del lst[0]
            else:
                del lst[-1]
        elif new_max > prev:
            ans = 'No'
            break

    return ans

num_cases = int(input())
cases = []
for i in range(num_cases):
    length = int(input())
    cases.append([int(i) for i in input().split()])

for i in cases:
    print(stackable(i))
