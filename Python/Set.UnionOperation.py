#Set .union() Operation
#https://www.hackerrank.com/challenges/py-set-union/problem

first = int(input())
a = set([int(i) for i in input().split()])
second = int(input())
b = set([int(i) for i in input().split()])

print(len(list(a.union(b))))
