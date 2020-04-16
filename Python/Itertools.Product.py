#itertools.product()
#https://www.hackerrank.com/challenges/itertools-product/problem

import itertools
A = input().split()
B = input().split()
A_ints = []
B_ints = []
for i in A:
    A_ints.append(int(i))

for j in B:
    B_ints.append(int(j))

string = ''
product = list(itertools.product(A_ints,B_ints))

print("".join(str(list(itertools.product(A_ints,B_ints)))).replace('[','').replace(']','').replace("),",')'))
