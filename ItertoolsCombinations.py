#itertools.combinations()
#https://www.hackerrank.com/challenges/itertools-combinations/problem

import itertools

user_input = input().split(' ')
word = user_input[0]
r = int(user_input[1])
word = sorted(word)

answer = []
for i in range(1, r+1):
    combinations = list(itertools.combinations(word,i))
    for j in combinations:
        answer.append(''.join(list(j)))

print("\n".join(answer))
