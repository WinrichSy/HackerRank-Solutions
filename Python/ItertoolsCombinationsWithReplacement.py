#itertools.combinations_with_replacement()
#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement
user_input = input().split(' ')
word = sorted(user_input[0])
num = int(user_input[1])

answer = []
combinations = combinations_with_replacement(word, num)
for i in combinations:
    answer.append(''.join(i))

print('\n'.join(answer))
