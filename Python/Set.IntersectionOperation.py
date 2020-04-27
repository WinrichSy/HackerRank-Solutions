#Set .intersection() Operation
#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

a_length = int(input())
a = set([int(i) for i in input().split()])
b_length = int(input())
b = set([int(i) for i in input().split()])

print(len(list(a.intersection(b))))
