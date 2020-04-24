# Set .difference() Operation
#https://www.hackerrank.com/challenges/py-set-difference-operation/problem

a_length = int(input())
a = input().split()
b_length = int(input())
b = input().split()

s = set(a)
print(len(s.difference(b)))
