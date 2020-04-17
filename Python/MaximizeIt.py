#Maximize It!
#https://www.hackerrank.com/challenges/maximize-it/problem

import itertools

#get first input
user_input = input().split(' ')
num_rows = int(user_input[0])
maximum = int(user_input[1])

rows = []
for i in range(num_rows):
    rows.append([int(x)**2 for x in input().split(' ')[1:]])

max = 0
possible_prod_combos = list(itertools.product(*rows))
for i in possible_prod_combos:
    if sum(i)%maximum > max:
        max = sum(i)%maximum

print(max)
