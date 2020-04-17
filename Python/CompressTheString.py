#Compress the String!
#https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
user_input = input()

answer = []

for key, num in groupby(user_input):
    answer.append((sum(1 for _ in num), int(key)))

print(str(answer).replace('[', '').replace(']', '').replace('),', ')'))
