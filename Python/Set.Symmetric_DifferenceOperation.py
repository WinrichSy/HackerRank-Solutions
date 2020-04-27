#Set .symmetric_difference() Operation
#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

a_length = int(input())
a = set([int(i) for i in input().split()])
b_length = int(input())
b = set([int(i) for i in input().split()])

print(len(list(a.symmetric_difference(b))))
