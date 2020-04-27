#No Idea!
#https://www.hackerrank.com/challenges/no-idea/problem

import collections

throwaway = input()
main_set = collections.Counter(input().split())
a = set(input().split())
b = set(input().split())

happy = 0
for key, val in main_set.items():
    if key in a:
        happy += val

sad = 0
for key, val in main_set.items():
    if key in b:
        sad += val

print(happy-sad)
